from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def my_index():
    return render_template("index.html", token="Hello Flask+React")


#import flask


#app = flask.Flask("__main__")


#@app.route("/")
#def my_index():
    #return flask.render_template("index.html", token="Hello Flask+React")


#app.run(debug=True)
