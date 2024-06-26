from flask import Flask
from flask_restx import Api
import os
from src.common.utils import db, ma
from src.routes.routes import Routes

#Esta parte crea la app
app = Flask(__name__)

app.config.from_object("settings.DeveloperConfig")
#app.config.from_object("settings.ProductionConfig")
'''
#Cargar nuestro entorno
if os.environ["FLASK_ENV"] == 'development':
    app.config.from_object("settings.DeveloperConfig")
else:
    app.config.from_object("settings.ProductionConfig")
'''

#Esto crea la Api para la app con un prefix
api = Api(app, prefix="/api/v1")\

#configuracion final de la db
db.init_app(app)
ma.init_app(app)

#Importar las rutas
Routes(api)