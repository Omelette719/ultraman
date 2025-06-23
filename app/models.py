from . import db

class Ultraman(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    human_host = db.Column(db.String(100))
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    description = db.Column(db.Text)
    image = db.Column(db.String(120))
