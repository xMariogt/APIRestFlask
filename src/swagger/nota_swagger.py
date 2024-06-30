from src.common.utils import api
from flask_restx import fields
from src.swagger.comentario_swagger import ComentarioSwagger

#Modelo para retornar la informacion de una nota
NotaSwagger = api.model('NotaSwagger', {
    'IDNOTA': fields.Integer,
    'DESCRIPCION': fields.String,
    'FECHA': fields.DateTime,
    'IDUSUARIO': fields.Integer,
    'COMENTARIOS': fields.Nested(ComentarioSwagger, as_list=True)
})

#Modelo para agregar la informacion de una nota
NotaPostSwagger = api.model('NotaPostSwagger', {
    'DESCRIPCION': fields.String,
    'FECHA': fields.DateTime,
    'IDUSUARIO': fields.Integer
})