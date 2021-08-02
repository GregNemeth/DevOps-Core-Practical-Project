from flask import Flask, jasonify, Response, request
app = Flask(__name__)

@app.route('/multiply', methods=['POST'])
def service_4():
    a = request.json['a']
    b = request.json['b']

    multi = a * b

    return jsonify(multi)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
