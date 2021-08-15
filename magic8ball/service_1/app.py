from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def home():

    a = requests.get('http://service-2:5000/randnum').json()
    b = requests.get('http://service-3:5000/randnum').json()
    
    multi = {'a': a, 'b': b}

    x = requests.post('http://service-4:5000/multiply', json=multi).json()
    
    hist = x['last_5']# should be simple list []
    m = x['m'] 
    return render_template('home.html', a=a, b=b, m=m, hist=hist, x=x)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
