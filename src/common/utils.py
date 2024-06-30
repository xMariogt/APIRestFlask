from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_restx import Api, fields

#Inicializar la api
api = Api(prefix="/api/v1")
#Inicializar las extensiones
db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()

#Objeto comun de respuesta a doc swagger

RespuestaGenerica = api.model('RespuestaGenerica', {
    'msg': fields.String
})