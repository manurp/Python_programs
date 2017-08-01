from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello():
    name = 'Manoj'
    html = render_template('index.html', name=name)
    return html
