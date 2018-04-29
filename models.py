from app import db,ma
from flask_sqlalchemy import SQLAlchemy

class Client(db.Model):

  id = db.Column(db.Integer, primary_key=True,index=True)
  name = db.Column(db.String(100))
  observation = db.Column(db.Text)
  contacts = db.relationship('Contact', backref='client', cascade='all, delete-orphan')

  def add(self):
    try:
      db.session.add(self)
      db.session.commit()
      return True
    except:
      return False

  def update(self):
    try:
      db.session.commit()
      return True
    except:
      return False

  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
      return True
    except:
      return False

  @classmethod
  def get_one(cls,**kwargs):
    try:
      return db.session.query(cls).filter_by(**kwargs).first( )
    except:
      return None

  @classmethod
  def get_all(cls,**kwargs):
    try:
      return db.session.query(cls).filter_by(**kwargs).all( )
    except:
      return None

class Contact(db.Model):

  id = db.Column(db.Integer, primary_key=True,index=True)
  type = db.Column(db.String(10))
  value = db.Column(db.String(100))
  client_id = db.Column(db.Integer, db.ForeignKey('client.id'),nullable=False)
  
  def add(self):
    try:
      db.session.add(self)
      db.session.commit()
      return True
    except:
      return False
  
  def update(self):
    try:
      db.session.commit()
      return True
    except:
      return False
  
  def delete(self):
    try:
      db.session.delete(self)
      db.session.commit()
      return True
    except:
      return False

  @classmethod
  def get_one(cls,**kwargs):
    try:
      return db.session.query(cls).filter_by(**kwargs).first( )
    except:
      return None

  @classmethod
  def get_all(cls,**kwargs):
    try:
      return db.session.query(cls).filter_by(**kwargs).all( )
    except:
      return None
      
class ContactSchema(ma.ModelSchema):
  class Meta:
    model = Contact

class ClientSchema(ma.ModelSchema):
  class Meta:
    model = Client