from flask import render_template, request, redirect, jsonify
from app import app, db
from sqlalchemy import desc
from app.models.tables import Task


@app.route('/todolist')
def todo():
    todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
    complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
    return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)


@app.route('/todolist/add', methods=['GET', 'POST'])
def todo_add():
    # todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
    # complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
    if request.method == 'POST':
        task_title = request.form['task_title']
        complete = False
        task = Task(task_title, complete)
        db.session.add(task)
        db.session.commit()
        # return redirect(request.url)
        # return task_title
        task = Task.query.filter_by(title=task_title).first()
        response = {'task_title': task_title, 'id': task.id}
        return response
    return render_template('todo/index.html')
    # return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)


@app.route('/todolist/update', methods=['POST'])
def todo_update():
    task_id = request.form["task_id"]
    task_title = request.form["task_title"]
    print('xxxxxxxxxxxxxxxxxx')
    print(task_title)
    print(task_id)
    # task_title = request.form['todo_task']
    task = Task.query.filter_by(id=task_id).first()
    task.title = task_title
    db.session.add(task)
    db.session.commit()
    # task.title = request.form['todo_task']
    # db.session.add(task)
    # db.session.commit()
    # todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
    # complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
    # if request.method == 'POST':
    #     task_title = request.form['todo_task']
    #     complete = False
    #     todo_task = Task(task_title, complete)
    #     db.session.add(todo_task)
    #     db.session.commit()
    #     # return redirect(request.url)
    #     # return task_title
    #     return task_title 
    # return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)
    # print(task)
    # return jsonify({'result' : 'success'})
    return render_template('todo/index.html')


# @app.route('/todolist/update/<task_title>', methods=['GET', 'POST'])
# def todo_update(task_title):
#     task = Task.query.filter_by(title=task_title).first()
#     task.title = "Clebiano4"
#     db.session.add(task)
#     db.session.commit()
#     # todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
#     # complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
#     # if request.method == 'POST':
#     #     task_title = request.form['todo_task']
#     #     complete = False
#     #     todo_task = Task(task_title, complete)
#     #     db.session.add(todo_task)
#     #     db.session.commit()
#     #     # return redirect(request.url)
#     #     # return task_title
#     #     return task_title 
#     # return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)
#     print(task)
#     return "Ok"

@app.route('/todolist/status', methods=['POST'])
def todo_status():
    task_id = request.form["task_id"]
    task_complete = eval(request.form["task_complete"])
    print('xxxxxxxxxxxxxxxxxx')
    print(task_complete)
    print(task_id)
    task = Task.query.filter_by(id=task_id).first()
    task.complete = task_complete
    db.session.add(task)
    db.session.commit()
    return render_template('todo/index.html')

@app.route('/todolist/delete', methods=['POST'])
def todo_delete():
    task_id = request.form["task_id"]
    # request.args.get("task_id")

    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    print(task_id)
    task = Task.query.filter_by(id=task_id).first()
    db.session.delete(task)
    db.session.commit()
    # # acho que essas duas linhas abaixo serão desnecessárias
    # todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
    # complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
    return render_template('todo/index.html')
    # , todo_tasks=todo_tasks, complete_tasks=complete_tasks)

    # task_title = request.args.get("task_title")
    # task = Task.query.filter_by(title=task_title).first()
    # db.session.delete(task)
    # db.session.commit()
    # # acho que essas duas linhas abaixo serão desnecessárias
    # todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
    # complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
    # return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)


# @app.route('/todolist/delete/<task_title>', methods=['POST'])
# def todo_delete(task_title):
#     task = Task.query.filter_by(title=task_title).first()
#     db.session.delete(task)
#     db.session.commit()
#     # acho que essas duas linhas abaixo serão desnecessárias
#     todo_tasks = Task.query.filter_by(complete=False).order_by(Task.id.desc()).all()
#     complete_tasks = Task.query.filter_by(complete=True).order_by(Task.id.desc()).all()
#     return render_template('todo/index.html', todo_tasks=todo_tasks, complete_tasks=complete_tasks)




# @app.route("/todolist")
# def todolist():
#     return render_template("todo/index.html")


# @app.route("/home")
# # @app.route("/")
# def index():
#     return "Olá Tamires!"


@app.route("/react")
def my_index():
    return render_template("index.html", token="Hello Flask+React")


# @app.route("/todolist/tasks/<int:id>", methods=['GET'])
# def task(id):
#     return "Task, %s!" % id


# @app.route("/add/<info>")
# @app.route("/add", defaults={"info": None})
# def add(info):
#     i = Task("Clebiano4", "Eu sou Clebianoooo", False)
#     print(i)
#     db.session.add(i)
#     db.session.commit()
#     return "Ok"


# @app.route("/search/<info>")
# @app.route("/search", defaults={"info": None})
# def search(info):
#     r = Task.query.filter_by(complete=False).all()
#     print(r)
#     return "Ok"


# @app.route("/delete/<info>")
# @app.route("/delete", defaults={"info": None})
# def delete(info):
#     r = Task.query.filter_by(title="Clebiano3").first()
#     db.session.delete(r)
#     db.session.commit()
#     print(r)
#     return "Ok"


# @app.route("/update/<info>")
# @app.route("/update", defaults={"info": None})
# def update(info):
#     r = Task.query.filter_by(title="Clebiano4").first()
#     r.title = "Clebiano5"
#     db.session.add(r)
#     db.session.commit()
#     print(r)
#     return "Ok"
