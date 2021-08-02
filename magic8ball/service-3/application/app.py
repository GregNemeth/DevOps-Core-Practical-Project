from random import choice
from flask import Flask


app = Flask(__name__)

@app.route('/')
@app.route('/service-3')
    
    def service-3():
        options = (
            1,
            2,
            3,
            2,
            1,
            3
        )
    return random.choice(options)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
