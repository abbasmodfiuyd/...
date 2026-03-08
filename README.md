# ToDo SaaS

A simple ToDo application built with Flask and SQLAlchemy.

## Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run migrations: `flask db upgrade`
3. Run the app: `python app.py`

## Docker

Build: `docker build -t todo-saas .`
Run: `docker run -p 5000:5000 todo-saas`