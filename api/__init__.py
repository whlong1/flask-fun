from flask import Flask
from flask_migrate import Migrate
from .models import db
from .views.cat import cat


def create_app(config):
  app = Flask(__name__)
  app.config.from_object(config)
  db.init_app(app)
  migrate = Migrate() 
  migrate.init_app(app, db)

  # Register Blueprints here
  app.register_blueprint(cat, url_prefix='/cats')
  
  return app
