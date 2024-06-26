from src.models.notacomentario_model import NotaComentarioModel
from src.schemas.comentario_schema import ComentarioSchema, ComentarioSchemaValidar
from src.schemas.nota_schema import NotaSchema, NotaSchemaValidar
from src.models.comentario_model import ComentarioModel
from src.common.utils import db
from flask_restx import Resource
from marshmallow import ValidationError
from flask import request

class ComentarioController(Resource):
    def get(self):
        try:
            comentariosdb = ComentarioModel.query.all()
            
            return ComentarioSchema(many=True).dump(comentariosdb), 200
        
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
class ComentarioControllerPost(Resource):
    def post(self):
        try:
            #Descomponemos la informacion
            comentarioJSON = request.json["COMENTARIO"]
            notaJSON = request.json["NOTA"]
            #Informacion del comentario
            comentariovalidar = ComentarioSchemaValidar(exclude=["IDCOMENTARIO",])
            comentariovalidar.load(comentarioJSON)
            #Se prepara el modelo a insertar en la db
            comentariodb = ComentarioSchema(transient=True).load(comentarioJSON)
            
            #Informacion de la nota
            notadb = NotaSchemaValidar().load(notaJSON)
            notadb = NotaSchema(transient=True).load(notaJSON)
            
            #Iniciar las transacciones
            db.session.begin()
            #Se inserta el comentario en la db
            db.session.add(comentariodb)
            #Se hace commit parcial
            db.session.flush()
            
            nota_comentario = NotaComentarioModel(IDNOTA=notadb.IDNOTA, IDCOMENTARIO=comentariodb.IDCOMENTARIO)
            db.session.add(nota_comentario)
            #Se hace commit final para confirmar la transaccion
            db.session.commit()
            
            return ComentarioSchema().dump(comentariodb), 201
        
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:  
            db.session.rollback()
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503   
        

class ComentarioControllerPut(Resource):
    def put(self):
        try:            
            comentariovalidar = ComentarioSchema(transient=True)
            comentario = comentariovalidar.load(request.json)
            
            comentariodb = ComentarioModel.query.where(ComentarioModel.IDCOMENTARIO == comentario.IDCOMENTARIO).one()
            
            comentariodb.DESCRIPCION = comentario.DESCRIPCION
            
            db.session.commit()
            
            return ComentarioSchema().dump(comentariodb), 200
        
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
        
class ComentarioControllerDelete(Resource):
    def delete(self, idcomentario):
        try:
            comentariodb = ComentarioModel.query.where(ComentarioModel.IDCOMENTARIO == idcomentario).one()
            
            db.session.delete(comentariodb)
            db.session.commit()
            
            return {"message": "Comentario eliminado"}, 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        

class ComentarioControllerById(Resource):
    def get(self, idcomentario):
        try:
            comentariodb = ComentarioModel.query.where(ComentarioModel.IDCOMENTARIO == idcomentario).one()
            
            return ComentarioSchema().dump(comentariodb), 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503