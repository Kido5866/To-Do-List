from __init__ import db
from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.DateTime(timezone=True), default=func.now(), primary_key=True)
    text = db.Column(db.String(500))



