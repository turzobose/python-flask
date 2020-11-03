from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route('/')
def hello():
	number = random.randint(1,10)
	return render_template("index.html", name ="Turzo", num = number)

@app.route('/goodbye')
def bye():
    return 'Bye bye'