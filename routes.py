import datetime
import json
from flask import Blueprint,request,jsonify,render_template

import models

# Routes for clients
clients_bp = Blueprint('clients', __name__)

@clients_bp.route('/clients', methods=['POST'] )
def clients_create( ):

  data = request.get_json( )

  try:
    client = models.Client(**data)
  except :
    return jsonify({'message' : 'Invalid parameter for client'}), 403

  if models.Client.get_one( id=client.id ) != None:
    return jsonify({'message' : 'Resource already exists'}), 409

  if not client.add( ) :
    return jsonify({'message' : 'Something is going wrong'}), 500

  return jsonify( { 'client' : models.ClientSchema( ).dump(client).data } ), 201
  ## end of clients_create method


@clients_bp.route('/clients', methods=['GET'] )
def clients_get_all( ):

  clientsList = models.Client().get_all( )

  return jsonify( { 'clients' : models.ClientSchema(many=True).dump(clientsList).data } ), 200
  ## end of clients_get_all method


@clients_bp.route('/clients/<int:id>', methods=['GET'] )
def clients_get(id):

  client = models.Client.get_one( id=id )

  if client == None:
    return jsonify({'message' : 'Resource not found'}), 404

  return jsonify( { 'client' : models.ClientSchema( ).dump(client).data } ), 200
  ## end of clients_get method


@clients_bp.route('/clients/<int:id>', methods=['PUT'] )
def clients_update(id):

  data = request.get_json()

  client = models.Client.get_one( id=id )

  if client == None:
    return jsonify({'message' : 'Resource not found'}), 404

  for key in data:
    if hasattr(client,key) and key != 'id' :
      setattr(client,key,data[key])

  if not client.update( ) :
    return jsonify({'message' : 'Something is going wrong'}), 500

  return jsonify( { 'client' : models.ClientSchema( ).dump(client).data } ), 200
  ## end of clients_update method


@clients_bp.route('/clients/<int:id>', methods=['DELETE'] )
def clients_delete(id):

  client = models.Client.get_one( id=id )

  if client == None:
    return jsonify({'message' : 'Resource not found'}), 404

  if not client.delete( ) :
      return jsonify({'message' : 'Something is going wrong'}), 500

  return 'This content response will not be displayed', 204
  ## end of clients_delete method

# Routes for contacts of clients
contacts_bp = Blueprint('contacts', __name__)

@contacts_bp.route('/clients/<int:id>/contacts', methods=['POST'] )
def contacts_create(id):

  data = request.get_json()

  try:
    contact = models.Contact(**data)
  except :
    return jsonify({'message' : 'Invalid parameters for contact'}), 403

  if models.Contact.get_one( id=contact.id ) != None:
    return jsonify({'message' : 'Resource already exists'}), 409

  contact.client = models.Client().get_one(id=id)

  if contact.client == None :
    return jsonify({'message' : 'resource not found'}), 404

  if not contact.add( ) :
    return jsonify({'message' : 'Something is going wrong'}), 500

  return jsonify( { 'contact' : models.ContactSchema( ).dump(contact).data } ), 201
  ## end of contacts_create method


@contacts_bp.route('/clients/<int:id>/contacts', methods=['GET'] )
def contacts_search(id):

  contactList = models.Contact().get_all(client_id=id)

  return jsonify( { 'contacts' : models.ContactSchema(many=True).dump(contactList).data } ), 200
  ## end of contacts_search method


@contacts_bp.route('/clients/<int:id>/contacts/<int:contact_id>', methods=['GET'] )
def contacts_get(id,contact_id):

  contact = models.Contact.get_one( client_id=id, id=contact_id )

  if contact == None:
    return jsonify({'message' : 'Resource not found'}), 404

  return jsonify( { 'contact' : models.ContactSchema( ).dump(contact).data } ), 200
  ## end of contacts_get method


@contacts_bp.route('/clients/<int:id>/contacts/<int:contact_id>', methods=['PUT'] )
def contacts_update(id,contact_id):

  data = request.get_json()
  
  contact = models.Contact.get_one( client_id=id, id=contact_id )

  if contact == None:
    return jsonify({'message' : 'Resource not found'}), 404

  for key in data:
    if hasattr(contact,key) and key != 'id' and key != 'client_id' :
      setattr(contact,key,data[key])

  if not contact.update( ) :
    return jsonify({'message' : 'Something is going wrong'}), 500

  return jsonify( { 'contact' : models.ContactSchema( ).dump(contact).data } ), 200
  ## end of contacts_update method


@contacts_bp.route('/clients/<int:id>/contacts/<int:contact_id>', methods=['DELETE'] )
def contacts_delete(id,contact_id):
  
  contact = models.Contact.get_one( client_id=id, id=contact_id )

  if contact == None:
    return jsonify({'message' : 'Resource not found'}), 404

  if not contact.delete( ) :
      return jsonify({'message' : 'Something is going wrong'}), 500

  return 'This content response will not be displayed', 204
  ## end of contacts_delete method

# Routes for clients
static_bp = Blueprint('static', __name__)

@static_bp.route('/' )
def index():
  year = datetime.date.today()
  return render_template("index.html",date_now=year)
  ## end of index method