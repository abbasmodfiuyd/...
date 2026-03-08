from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from flask_migrate import Migrate
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    q = request.args.get('q', '')
    status_filter = request.args.get('status', '')
    priority_filter = request.args.get('priority', '')
    due_filter = request.args.get('due', '')
    sort_by = request.args.get('sort', 'created_at')

    tasks_query = Task.query

    if q:
        tasks_query = tasks_query.filter(
            db.or_(Task.title.contains(q), Task.description.contains(q))
        )

    if status_filter:
        tasks_query = tasks_query.filter(Task.status == status_filter)

    if priority_filter:
        tasks_query = tasks_query.filter(Task.priority == int(priority_filter))

    from datetime import datetime, timedelta
    now = datetime.utcnow()
    if due_filter == 'overdue':
        tasks_query = tasks_query.filter(Task.due_date < now)
    elif due_filter == 'today':
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        today_end = today_start + timedelta(days=1)
        tasks_query = tasks_query.filter(Task.due_date.between(today_start, today_end))
    elif due_filter == 'this_week':
        week_start = now - timedelta(days=now.weekday())
        week_start = week_start.replace(hour=0, minute=0, second=0, microsecond=0)
        week_end = week_start + timedelta(days=7)
        tasks_query = tasks_query.filter(
            Task.due_date.between(week_start, week_end))

    if sort_by == 'due_date':
        tasks_query = tasks_query.order_by(Task.due_date)
    elif sort_by == 'priority':
        tasks_query = tasks_query.order_by(Task.priority.desc())
    elif sort_by == 'title':
        tasks_query = tasks_query.order_by(Task.title)
    else:
        tasks_query = tasks_query.order_by(Task.created_at.desc())

    tasks = tasks_query.all()
    return render_template('index.html',
                           tasks=tasks,
                           q=q,
                           status_filter=status_filter,
                           priority_filter=priority_filter,
                           due_filter=due_filter,
                           sort_by=sort_by)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form.get('title')
    description = request.form.get('description')
    priority = int(request.form.get('priority', 1))
    due_date_str = request.form.get('due_date')
    due_date = datetime.fromisoformat(due_date_str) if due_date_str else None
    if title:
        task = Task(title=title, description=description, priority=priority, due_date=due_date)
        db.session.add(task)
        db.session.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
