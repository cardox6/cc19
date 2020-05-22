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

<<<<<<< HEAD
@app.route('/global_charts')
def charts():
    return render_template('global_charts.html', title="Global Charts")

@app.route('/continents_charts'
def continents_charts():
    return render_template('continents_charts.html', title='Continents Charts')
=======
@app.route('/charts')
def charts():
    return render_template('charts.html', title="Charts")
>>>>>>> 42d6d51... hex background. Included pie chart, responsive layout.
