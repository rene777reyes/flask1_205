from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

app = Flask(__name__)
bootstrap = Bootstrap5(app)

@app.route('/')
def hello():
    return 'Hello world from Flask'

@app.route('/acronym')
def fav_acron():
    acr_title = '<h1> Fav acronyms </h1>'
    acr1 = '<p>Nico R. : goomr</p>'
    acr2 = '<p>Pablo N. : amp</p>'
    acr3 = '<p>Amparo P. : ily</p>'
    return acr_title + acr1 + acr2 + acr3

@app.route('/rene')
def my_fav_acron():
    return render_template('template.html')
    