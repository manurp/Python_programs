from flask import Flask, render_template

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


@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    return render_template('routing/author.html',
                           author=AUTHORS_INFO[authors_last_name])
