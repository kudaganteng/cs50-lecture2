import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    text = "Hello World"
    return render_template("index.html", headline = text)

@app.route("/pagetwo")
def pagetwo():
    return render_template("pagetwo.html")


@app.route("/newyear")
def newyear():
    dateNow = datetime.datetime.now()
    newYear = dateNow.month == 1 and dateNow.day == 1
    newYear = True
    return render_template("index.html", newyear = newYear)

@app.route("/hello", methods=["POST"])
def hello():
    username = request.form.get("username")
    password = request.form.get("password")
    return render_template("login.html", username = username, password = password)