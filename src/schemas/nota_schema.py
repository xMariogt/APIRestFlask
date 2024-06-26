from src.schemas.usuario_schema import UsuarioSchema
from src.models.nota_model import NotaModel
from src.common.utils import ma
from marshmallow import Schema, fields, validate

class NotaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaModel
        ordered = True
        load_instance = True
        include_fk = True #incluye la llave foranea
        include_relationships = True #incluye las relaciones
        
    #relationships
    USUARIO = fields.Nested(UsuarioSchema())   
    COMENTARIOS = fields.Nested("ComentarioSchema", many=True)

class NotaSchemaValidar(Schema):
    IDNOTA = fields.Integer(required=True)
    DESCRIPCION = fields.String(required=True)
    FECHA = fields.DateTime(required=True)
    IDUSUARIO = fields.Integer(required=True, validate = validate.Range(min=1, max=99))