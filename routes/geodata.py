from flask import Blueprint, request, jsonify 
from models import db, geo_routes

geodata = Blueprint('geodata', __name__)

@geodata.route('/api/geodata', methods=['GET'])
def get_geodata():
   geodata_list = geo_routes.query.all()
   return jsonify([
         {
            'id': data.id,
            'name': data.name,
            'geometry': data.geometry
         } 
         for data in geodata_list
   ])

@geodata.route('/api/geodata', methods=['POST'])
def add_geodata():
   data = request.json
   if 'name' not in data or 'geometry' not in data:
      return jsonify({'error': 'Missing data'}), 400
   
   new_geodata = geo_routes(name=data['name'], geometry=data['geometry'])
   db.session.add(new_geodata)
   db.session.commit()
   return jsonify({'message': 'Data added successfully'}), 201