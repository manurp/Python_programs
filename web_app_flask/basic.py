from flask import Flask, render_template

app = Flask(__name__)

posts_list = [
    {
        'author': 'Manoj',
        'title': 'FIrst blog',
        'date': 'April 17 2018',
        'content': 'first blog using python and flask'
    },
    {
        'author': 'Bhoomi',
        'title': 'Secod blog',
        'date': 'April 17 2018',
        'content': 'Second blog using html and flask'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=posts_list, title='Posts')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
