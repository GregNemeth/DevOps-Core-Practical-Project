from . import app, db
from .models import Nexus, History
from flask import jsonify, request

@app.route('/multiply', methods=['POST'])
def service_4():
    a = request.json['a']
    b = request.json['b']
    m = (a * b)*10
    prophecy = Nexus.query.filter_by(id=m).first()
    
    last_5 = History.query.order_by(History.id.desc()).limit(5).all()
    last = []
    
    for item in last_5:
        last.append(item.res)
    history = History(a=a,b=b,x=m,res=prophecy.omen)
    db.session.add(history)
    db.session.commit()
    
    xur = {
        "m":m,
        "prophecy":prophecy.omen,
        "last_5":last
    }



    return jsonify(xur)

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
