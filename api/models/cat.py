from flask import jsonify
from datetime import datetime
from . import db

class Cat(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    breed = db.Column(db.String(100))
    description = db.Column(db.String(250))
    age = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
      return '<Cat %r>' % (self.name)

    def serialize(self):
      return {
        "id": self.id,
        "name": self.name,
        "breed": self.breed,
        "description": self.description,
        "age": self.age,
        "created_at": str(self.created_at),
      }
