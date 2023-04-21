from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("/home/spencer/Documents/Programs/IT-390-Group-1/graphiccard.html")

if __name__ == '__main__':
    app.run(debug=1)
