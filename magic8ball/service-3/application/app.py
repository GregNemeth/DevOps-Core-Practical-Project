from flask import Flask, jsonify
from random import choice


app = Flask(__name__)

@app.route('/randnum', methods=['GET'])
    
    def service-2():
        options = (
            1,
            2,
            3,
            2,
            1,
            3
        )
    return jsonify(random.choice(options))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
