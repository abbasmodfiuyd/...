from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    q = request.args.get('q', '')
    tasks_query = Task.query
    if q:
        tasks_query = tasks_query.filter(
            db.or_(Task.title.contains(q), Task.description.contains(q))
        )
    tasks = tasks_query.all()
    return render_template('index.html', tasks=tasks, q=q)

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