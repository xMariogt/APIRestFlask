from flask_restx import Resource
from src.common.utils import db
from flask import request
from marshmallow import ValidationError
from src.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import UsuarioSchema, UsuarioSchemaValidar

class UsuarioController(Resource):
    def get(self):
        try:
            
            #query = UsuarioModel.query.all()
            query = db.session.execute(db.select(UsuarioModel)).scalars()
            usuario_schema = UsuarioSchema(many=True)
            
            return usuario_schema.dump(query), 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo.\n{e}"}, 503
        

class UsuarioControllerPost(Resource):
    def post(self):
        try:
            usuariovalidar = UsuarioSchemaValidar()
            usuariovalidar.load(request.json)
            
            usuariovalidar = UsuarioSchema(transient=True)
            #usuariodb = usuariovalidar.load(request.json, session=db.session)
            usuariodb = usuariovalidar.load(request.json)
            
            db.session.add(usuariodb)
            db.session.commit()
            
            return UsuarioSchema().dump(usuariodb), 201
        
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
class UsuarioControllerPut(Resource):
    def put(self):
        try:
            
            usuariovalidar = UsuarioSchema(transient=True)
            usuario = usuariovalidar.load(request.json)
            
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == usuario.IDUSUARIO).one()
        
            usuariodb.NOMBRE = usuario.NOMBRE
            
            db.session.commit()
            
            return UsuarioSchema().dump(usuariodb), 200
        
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
class UsuarioControllerDelete(Resource):
    def delete(self, idusuario):
        try:
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == idusuario).one()
            db.session.delete(usuariodb)
            db.session.commit()
            
            return {"message": "Usuario eliminado"}, 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
    
class UsuarioControllerById(Resource):
    def get(self, idusuario):
        try:
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == idusuario).one()
            
            return UsuarioSchema().dump(usuariodb), 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503