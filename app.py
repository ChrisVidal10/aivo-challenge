import os
from flask import Flask
from flask_restful import Api
from ext import ma, migrate, db
from resources.routes import initialize_routes
from resources.exceptions import exceptions
import config

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Init settings
app.config.from_object(config)

# Init db
db.init_app(app)

# Init ma
ma.init_app(app)

# Init migrate
migrate.init_app(app, db)

#Init flask restful
api = Api(app, errors=exceptions)

# Init resources endpoints 
initialize_routes(api)

# Run Server
if __name__ == '__main__':
  app.run()
