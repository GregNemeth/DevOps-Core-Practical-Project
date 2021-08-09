from flask import Flask, jsonify
import random


app = Flask(__name__)

@app.route('/randnum', methods=['GET'])
    
def service_2():
    options = (
        1,
        2,
        3,
        4,
        2,
        4,
        1,
        3
    )
    return jsonify(random.choice(options))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
