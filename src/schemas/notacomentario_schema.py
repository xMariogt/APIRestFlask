from src.models.notacomentario_model import NotaComentarioModel
from src.common.utils import ma
from marshmallow import Schema, fields, validate

class ComentarioSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = NotaComentarioModel
        ordered = True
        load_instance = True
        #include_relationships = True #incluye las relaciones
        #include_fk = True #incluye la llave foranea
        
class NotaComentarioSchemaValidar(Schema):
    IDNOTA = fields.Integer(required=True)
    IDCOMENTARIO = fields.Integer(required=True)