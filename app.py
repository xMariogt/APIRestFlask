from flask import Flask
import os
from src.common.utils import db, ma, jwt, api
from src.routes.routes import Routes

#Esta parte crea la app
app = Flask(__name__)

#app.config.from_object("settings.DeveloperConfig")
#app.config.from_object("settings.ProductionConfig")

#Cargar nuestro entorno
#Para que esto funcione si debo hacer el export de la Variable de entorno
if os.environ["FLASK_ENV"] == 'development':
    app.config.from_object("settings.DeveloperConfig")
else:
    app.config.from_object("settings.ProductionConfig")


#Esto inicializa la Api para la app con un prefix
api.init_app(app)

#configuracion final de la db
db.init_app(app)
ma.init_app(app)
jwt.init_app(app)

#Importar las rutas
Routes(api)