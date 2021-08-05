from application import db

class Nexus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    omen = db.Column(db.String(200), nullable=False)