from flask import Blueprint, jsonify, request
from sqlalchemy.orm import joinedload

from .. import db
from ..models.cat import Cat

cat = Blueprint('cats', 'cat')

@cat.route('/', methods=["GET"])
def index():
  cats = Cat.query.all()
  return jsonify([cat.serialize() for cat in cats])

@cat.route('/<id>', methods=["GET"])
def show(id):
  cat = Cat.query.filter_by(id=id).first().serialize()
  return cat

@cat.route('/', methods=["POST"]) 
def create():
  data = request.get_json()
  cat = Cat(**data)
  db.session.add(cat)
  db.session.commit()
  return cat.serialize()
