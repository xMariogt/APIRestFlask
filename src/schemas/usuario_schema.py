from src.models.usuario_model import UsuarioModel
from marshmallow import Schema, fields, validate
from src.common.utils import ma

class UsuarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = UsuarioModel
        ordered = True
        load_instance = True
        include_relationships = True #incluye las relaciones
        
    #relationships
    COMENTARIOS = fields.Nested("ComentarioSchema", many=True)
    NOTAS = fields.Nested("NotaSchema", many=True, exclude=("USUARIO",))
        
class UsuarioSchemaValidar(Schema):
    IDUSUARIO = fields.Integer(required=True, validate = validate.Range(min=1, max=99))
    NOMBRE = fields.String(required=True)
    CORREO = fields.Email(required=True)
    CONTRASENIA = fields.String(required=True)
    
class UsuarioSchemaLogin(Schema):
    CORREO = fields.Email(required=True)
    CONTRASENIA = fields.String(required=True)