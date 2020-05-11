from flask import render_template, url_for
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Index")

@app.route('/infographics')
def infographics():
    return render_template('infographics.html', title="Infographics")

@app.route('/aboutcovid')
def aboutcovid():
    return render_template('aboutcovid.html', title="About Covid 19")

@app.route('/check')
def check():
    return render_template('check.html', title="Check Yourself")