from flask import render_template
from app import app, db
from app.models.tables import Task


# @app.route("/home")
# # @app.route("/")
# def index():
#     return "Olá Tamires!"


@app.route("/")
@app.route("/todolist")
def my_index():
    return render_template("index.html", token="Hello Flask+React")


@app.route("/todolist/tasks/<int:id>", methods=['GET'])
def task(id):
    return "Task, %s!" % id


@app.route("/add/<info>")
@app.route("/add", defaults={"info": None})
def add(info):
    i = Task("Clebiano4", "Eu sou Clebianoooo", False)
    print(i)
    db.session.add(i)
    db.session.commit()
    return "Ok"


@app.route("/search/<info>")
@app.route("/search", defaults={"info": None})
def search(info):
    r = Task.query.filter_by(complete=True).all()
    print(r)
    return "Ok"


@app.route("/delete/<info>")
@app.route("/delete", defaults={"info": None})
def delete(info):
    r = Task.query.filter_by(name="Clebiano3").first()
    db.session.delete(r)
    db.session.commit()
    print(r)
    return "Ok"


@app.route("/update/<info>")
@app.route("/update", defaults={"info": None})
def update(info):
    r = Task.query.filter_by(name="Clebiano4").first()
    r.name = "Clebiano5"
    db.session.add(r)
    db.session.commit()
    print(r)
    return "Ok"
