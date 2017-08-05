"""HTML generated from data pulled from a database.
In this example we're pulling data from a simple sqlite3 database and
building an HTML template with it.
Requirements:
 * A database created with some data about authors inside.
"""
import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)


@app.route('/')
def hello_world():
    db_connection = connect_db()
    cursor = db_connection.execute('SELECT id, name FROM author;')
    authors = [dict(id=row[0], name=row[1]) for row in cursor.fetchall()]
    return render_template('database/authors.html', authors=authors)
