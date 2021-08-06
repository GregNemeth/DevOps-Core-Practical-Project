from application import app, db
from application.models import Nexus, History
from flask import jsonify, request

@app.route('/multiply', methods=['POST'])
def service_4():
    a = request.json['a']
    b = request.json['b']
    m = a * b
    prophecy = Nexus.query.filter_by(id=m).first()
    history = History(a=a,b=b,x=m)
    db.session.add(history)
    db.session.commit

    x = {
        "m":m,
        "prophecy":prophecy.omen
    }

    return jsonify(x)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)