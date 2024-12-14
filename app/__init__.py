from flask import Flask

def create_app():
  app = Flask(__name__)
  
  # Configure app settings
  app.config['SECRET_KEY'] = 'your_secret_key'
  app.config['DATABASE'] = 'face_database.db'
  
  from . import routes
  app.register_blueprint(routes.bp)
  
  return app