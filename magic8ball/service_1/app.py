from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():

    a = requests.get('http://service_2:5000/randnum').json()
    b = requests.get('http://service_3:5000/randnum').json()

    multi = {'a': a, 'b': b}

    x = requests.post('http://service_4:5000/multiply', json=multi).json()

    return render_template('home.html', a=a, b=b, x=x, hist=hist)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
