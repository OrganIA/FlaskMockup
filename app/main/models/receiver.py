from app import db

class Receiver(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    birthday = db.Column(db.DateTime)
    arrival = db.Column(db.DateTime)
    needed_organ = db.Column(db.String)
    gender = db.Column(db.String)
    abo = db.Column(db.String)
