from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color: green'>Hello Flask</h1> <p>This is the home page</p>"


@app.route('/manu')
def hello():
    return '<h2>Hello manu</h2>'


@app.route('/profile/<username>')
def say_hi(username):
    return '<h3>Hi {}</h3>'.format(username)


@app.route('/post/<int:post_id>')
def print_id(post_id):
    return '<p style="color:blue">The id is {}</p>'.format(post_id)


if __name__ == "__main__":
    app.run()
