from flask import Flask, request
from application import app
import requests


@app.route('/')
def home():

    a = requests.get('http://service-2:5000/randnum').json()
    b = requests.get('http://service-3:5000/randnum').json()

    multi = {'a': a, 'b': b}

    x = requests.post('http://service-4:5000/multiply', json=multi).json()