from src.common.utils import api
from flask_restx import fields

ComentarioSwagger = api.model('ComentarioSwagger', {
    'IDCOMENTARIO': fields.Integer,
    'DESCRIPCION': fields.String,
    'FECHA': fields.DateTime,
    'IDUSUARIO': fields.Integer
})