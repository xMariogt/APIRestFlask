from src.schemas.usuario_schema import UsuarioSchema
from src.models.comentario_model import ComentarioModel
from src.common.utils import ma
from marshmallow import Schema, fields, validate

class ComentarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ComentarioModel
        ordered = True
        load_instance = True
        include_relationships = True #incluye las relaciones
        include_fk = True #incluye la llave foranea
        
class ComentarioSchemaValidar(Schema):
    IDCOMENTARIO = fields.Integer(required=True)
    DESCRIPCION = fields.String(required=True)
    FECHA = fields.DateTime(required=True)
    IDUSUARIO = fields.Integer(required=True, validate = validate.Range(min=1, max=99))