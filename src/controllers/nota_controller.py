from flask_jwt_extended import jwt_required
from flask_restx import Resource
from src.common.utils import db
from src.models.nota_model import NotaModel
from src.schemas.nota_schema import NotaSchema, NotaSchemaValidar
from flask import request
from marshmallow import ValidationError

class NotaController(Resource):
    @jwt_required()
    def get(self):
        try:
            #Consulta a la base de datos
            query = db.session.execute(db.select(NotaModel)).scalars()
            #Serializacion de los datos
            notas_schema = NotaSchema(many=True)
            #Retorno de los datos
            return notas_schema.dump(query), 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo.\n{e}"}, 503
    


#Controlador POST
class NotaControllerPost(Resource):
    @jwt_required()
    def post(self):
        try:
            notasValidar = NotaSchemaValidar(exclude=["IDNOTA",])
            notasValidar.load(request.json)

            notasValidar = NotaSchema(transient=True)
            notasdb = notasValidar.load(request.json)

            db.session.add(notasdb)
            db.session.commit()

            return NotaSchema().dump(notasdb), 201

        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
        
        
class NotaControllerPut(Resource):
    @jwt_required()
    def put(self):
        try:
            #Validar los datos
            notasValidar = NotaSchema(transient=True)
            nota = notasValidar.load(request.json)

            #Consultar la data
            notadb = db.session.execute(db.select(NotaModel).where(NotaModel.IDNOTA == nota.IDNOTA)).scalar_one()
            notadb.DESCRIPCION = nota.DESCRIPCION
            notadb.FECHA = nota.FECHA
            
            db.session.commit()

            return NotaSchema().dump(notadb), 200
        
        #except NotResultFound:
            #return {"message": "La nota no existe"}, 404
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo.\n{e}"}, 503
        
        
class NotaControllerDelete(Resource):
    @jwt_required()
    def delete(self, idnota):
        try:
            
            notadb = db.session.execute(db.select(NotaModel).where(NotaModel.IDNOTA == idnota)).scalar_one()
            db.session.delete(notadb)
            db.session.commit()
            
            return {"message": "Nota eliminada"}, 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo.\n{e}"}, 503
        
class NotaControllerById(Resource):
    @jwt_required()
    def get(self, idnota):
        try:
            notadb = db.session.execute(db.select(NotaModel).where(NotaModel.IDNOTA == idnota)).scalar_one()
            notas_schema = NotaSchema()
                #Retorno de los datos
            return notas_schema.dump(notadb), 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo.\n{e}"}, 503
    
        