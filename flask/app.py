from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1 style='color: green'>Hello Flask</h1> <p>This is the home page</p>"


if __name__ == "__main__":
    app.run()
