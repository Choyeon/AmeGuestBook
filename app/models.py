from datetime import datetime
from app import db


class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255))
    name = db.Column(db.String(20))
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)
