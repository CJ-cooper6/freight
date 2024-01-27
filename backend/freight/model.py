from datetime import datetime
from backend.database import db


class Freight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    piece = db.Column(db.DECIMAL(10, 4))
    cube = db.Column(db.DECIMAL(10, 4))
    weight = db.Column(db.DECIMAL(10, 4))
    imprest = db.Column(db.DECIMAL(10, 4))
    package_number = db.Column(db.Integer)
    room = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    update_at = db.Column(db.DateTime, default=datetime.utcnow)
