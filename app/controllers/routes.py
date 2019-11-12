from flask import render_template, request, redirect, jsonify
from app import app, db
from sqlalchemy import desc
from app.models.models import Task


@app.route('/todolist')
def todo():
    todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
    complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
    return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)


@app.route('/todolist/add', methods=['GET', 'POST'])
def todo_add():
    if request.method == 'POST':
        task_title = request.form['task_title']
        complete = False
        task = Task(task_title, complete)
        db.session.add(task)
        db.session.commit()
        task = Task.query.filter_by(title=task_title).first()
        response = {'task_title': task_title, 'id': task.id}
        return response
    return render_template('todo/index.html')


@app.route('/todolist/update', methods=['POST'])
def todo_update():
    task_id = request.form["task_id"]
    task_title = request.form["task_title"]
    task = Task.query.filter_by(id=task_id).first()
    task.title = task_title
    db.session.add(task)
    db.session.commit()
    return render_template('todo/index.html')


@app.route('/todolist/status', methods=['POST'])
def todo_status():
    task_id = request.form["task_id"]
    task_complete = eval(request.form["task_complete"])
    task = Task.query.filter_by(id=task_id).first()
    task.complete = task_complete
    db.session.add(task)
    db.session.commit()
    return render_template('todo/index.html')


@app.route('/todolist/delete', methods=['POST'])
def todo_delete():
    task_id = request.form["task_id"]
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    return render_template('todo/index.html')
