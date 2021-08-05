from application import app
from application.models import Nexus
from flask import jsonify, request

@app.route('/multiply', methods=['POST'])
def service_4():
    a = request.json['a']
    b = request.json['b']
    m = a * b
    prophecy = Nexus.query.filter_by(id=m).first()

    x = {
        m:prophecy
    }

    return jsonify(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)