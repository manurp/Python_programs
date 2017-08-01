from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = 'Manoj'
    html = render_template('index.html', name=name)  # default: look for index.html in templates directory
    return html
