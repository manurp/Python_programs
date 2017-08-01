from flask import Flask
from flask import render_template_string  # !Important

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Templates"
    html = """
        <html>
        <head><title>Templates</title>
        </head>
        <body>
            <h1>Welcome to {{library}} Flask!</h1>
            <ul>
                {% for author in authors %}
                <li>{{author}}</li>
                {%endfor%}</ul>
                </body>
        </html>
    """
    authors = ["Manoj Poojari", "Bhoomika R. Poojari", "Sathya Jathan"]
    rendered_html = render_template_string(html, library=library_name, authors=authors)
    return rendered_html
