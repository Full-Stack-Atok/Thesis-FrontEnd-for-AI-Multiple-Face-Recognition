from flask import Blueprint, render_template, request, jsonify
from . import recognition, registration

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
  return render_template('index.html')

@bp.route('/register', methods=['POST'])
def register_face():
    data = request.json
    result = registration.register_face(data['image'], data['id'], data['name'])
    return jsonify(result) 
  
@bp.route('/recognize', methods=['POST'])
def recognize_face():
  data = request.json
  result = recognition.recognize_face(data['image'])
  return jsonify(result)
