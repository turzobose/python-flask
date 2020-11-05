from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route('/')
def hello():
    number = random.randint(1,100)
    return render_template("index.html", num=number)

@app.route('/hello')
def bye():
    name = request.args.get("name")
    if not name:
        return render_template("failure.html")
    return render_template("hello.html", name=name)
