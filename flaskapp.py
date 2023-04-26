from flask import Flask, render_template
from dbconnector import dbResult  # import database connector class from dbconnector.py

results = dbResult()  # instantiate object

app = Flask(__name__)


@app.route('/')
def index():
    test = 'HELLO'
    return render_template("graphiccard.html")


if __name__ == '__main__':
    app.run(debug=1)
