from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    html = """
    <html>
        <h1>Authors List</h1>
        {authors_li}
    </html>
    """
    authors = ['Manoj Poojari', 'Satya', 'Bhoomi', 'Shwetha']
    authors_list = "<ul>"
    authors_list += "\n".join(["<li>{author}</li>".format(author=author) for author in authors])
    authors_list += "</ul>"

    return html.format(authors_li=authors_list)
