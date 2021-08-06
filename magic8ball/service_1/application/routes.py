from flask import render_template
from application import app
from service_4.application.models import History
import requests


@app.route('/', methods=["POST", "GET"])
def home():

    a = requests.get('http://service_2:5000/randnum').json()
    b = requests.get('http://service_3:5000/randnum').json()

    multi = {'a': a, 'b': b}

    x = requests.post('http://service_4:5000/multiply', json=multi).json()

    hist = History.query.order_by(History.id.desc()).limit(5).all()

    return render_template('home.html', a=a, b=b, x=x, hist=hist)