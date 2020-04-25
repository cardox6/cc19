from flask import render_template, url_for
from app import app

posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Index")

@app.route('/infographics')
def infographics():
    return render_template('infographics.html', title="Infographics")

@app.route('/blog')
def blog():
    return render_template('blog.html', title="Blog")

@app.route('/aboutcovid')
def aboutcovid():
    return render_template('aboutcovid.html', title="About Covid 19")