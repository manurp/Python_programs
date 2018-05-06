from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.forms import RegistrationForm, LoginForm

posts_list = [
    {
        'author': 'Manoj',
        'title': 'First blog',
        'date': 'April 17 2018',
        'content': 'first blog using python and flask'
    },
    {
        'author': 'Bhoomi',
        'title': 'Secod blog',
        'date': 'June 19 2018',
        'content': 'Second blog using html and flask'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts_list)


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=posts_list, title='Posts')


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account Created for {}!'.format(form.username.data), 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@m.com' and form.password.data == 'pass':
            flash('You have been logged in!!', 'success')
            return redirect(url_for('home'))
        else:
            flash('login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
