from application import db

class Nexus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    omen = db.Column(db.String(200), nullable=False)

class History(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    a = db.Column(db.Integer, nullable=False)
    b = db.Column(db.Integer, nullable=False)
    x = db.Column(db.Integer, nullable=False)
    res = db.Column(db.String(200), nullable=False)
