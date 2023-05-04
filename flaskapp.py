from flask import Flask, render_template, send_file
from dbconnector import dbResult  # import database connector class from dbconnector.py

results = dbResult()  # instantiate object

app = Flask(__name__)


@app.route('/')
def index():
    return send_file('static/html/index.html')

@app.route('/about')
def about():
    return send_file('static/html/about.html')

@app.route('/contact')
def contact():
    return send_file('static/html/contact.html')

@app.route('/graphiccard')
def graphiccard():
    return send_file('static/html/graphiccard.html')

@app.route('/marketplace')
def marketplace():
    return send_file('static/html/marketplace.html')

@app.route('/listing')
def listing():
    return render_template('listing.html')

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory(os.path.join(app.root_path, 'static'), path)


if __name__ == '__main__':
    app.run(debug=1)
