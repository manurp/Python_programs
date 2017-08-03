"""Raising custom erros.
Sometimes users will perform invalid actions
(either intentionally, or unintentionally)
In order to protect our application and also inform the user about her
mistake, we'll need to raise custom errors.
The HTTP protocol support error responses with different
status codes. For example:
* 4XX: Client Error.
       These errors are caused by user's fault. The user tried to perform
       an invalid operation, forgot to send some data, etc.
* 5XX: Server Error.
       These are errors generated in our end. The error was produced
       in the server.
If we're raising an error after a user's action, we'll probably raise a `4XX`.
The most common `4XX` errors are:
* 404 (Not Found): Resource not found
* 400 (Bad Request): A general error. Used for example if the user forgets
                     to submit important data.
* 401 (Unauthorized): The user hasn't been authorized to access this resource.
                      Usually, will need to perform some type of authentication
* 403 (Forbidden): Similar to 401, but in this case the server knows who
                   the user is, but that user is not allowed to access
                   that resource. Usually an unprivileged user is trying to
                   perform admin actions.
Useful Resources:
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#4xx_Client_Error
https://en.wikipedia.org/wiki/List_of_HTTP_status_codes#5xx_Server_Error
"""

from flask import Flask, render_template, abort

app = Flask(__name__)

AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/7/75/Edgar_Allan_Poe_2_retouched_and_transparent_bg.png'
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
        'picture': 'https://upload.wikimedia.org/wikipedia/commons/c/cf/Jorge_Luis_Borges_1951%2C_by_Grete_Stern.jpg'
    }
}


@app.route('/')
def authors():
  return render_template('routing/authors.html')


@app.route('/author/<string:authors_last_name>')
def author(authors_last_name):
  if authors_last_name not in AUTHORS_INFO:
    abort(404)
  return render_template('routing/author.html',
                         author=AUTHORS_INFO[authors_last_name])


@app.route('/author/<string:authors_last_name>/edit')
def author_admin(authors_last_name):
  abort(401)


@app.errorhandler(404)  # If not present default 404 message is displayed
def not_found(error):
  return render_template('routing/404.html'), 404
