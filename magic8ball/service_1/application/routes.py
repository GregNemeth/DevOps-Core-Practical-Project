from flask import Flask, request, render_template
from application import app
import requests


@app.route('/', methods=["POST", "GET"])
def home():

    a = requests.get('http://service_2:5000/randnum').json()
    b = requests.get('http://service_3:5000/randnum').json()

    multi = {'a': a, 'b': b}

    x = requests.post('http://service_4:5000/multiply', json=multi).json()

    

    return render_template('home.html', a=a, b=b, x=x)