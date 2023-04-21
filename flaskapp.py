from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    test = 'HELLO'
    return render_template("graphiccard.html")

if __name__ == '__main__':
    app.run(debug=1)
