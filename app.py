from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from configs import create_configs

app = Flask(__name__,template_folder='static')
app = create_configs(app)

db = SQLAlchemy(app,session_options={'autoflush': True})
ma = Marshmallow(app)

from models import *

# import routes from file
from routes import clients_bp,contacts_bp,static_bp
app.register_blueprint( clients_bp )
app.register_blueprint( contacts_bp )
app.register_blueprint( static_bp )

if __name__ == "__main__":
  app.run(debug=True,port=80)