import datetime
from flask_restx import Resource
from flask_jwt_extended import create_access_token, jwt_required
from src.common.utils import db
from flask import request
from marshmallow import ValidationError
from sqlalchemy.exc import NoResultFound
from src.models.usuario_model import UsuarioModel
from src.schemas.usuario_schema import UsuarioSchema, UsuarioSchemaLogin, UsuarioSchemaValidar

class UsuarioController(Resource):
    @jwt_required()
    def get(self):
        try:
            
            #query = UsuarioModel.query.all()
            query = db.session.execute(db.select(UsuarioModel)).scalars()
            usuario_schema = UsuarioSchema(many=True)
            
            return usuario_schema.dump(query), 200
        
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo.\n{e}"}, 503
        

class UsuarioControllerPost(Resource):
    @jwt_required()
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
    @jwt_required()
    def put(self):
        try:
            
            usuariovalidar = UsuarioSchema(transient=True)
            usuario = usuariovalidar.load(request.json)
            
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == usuario.IDUSUARIO).one()
        
            usuariodb.NOMBRE = usuario.NOMBRE
            usuariodb.CORREO = usuario.CORREO
            
            db.session.commit()
            
            return UsuarioSchema().dump(usuariodb), 200
        
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
class UsuarioControllerDelete(Resource):
    @jwt_required()
    def delete(self, idusuario):
        try:
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == idusuario).one()
            db.session.delete(usuariodb)
            db.session.commit()
            
            return {"message": "Usuario eliminado"}, 200
        
        except NoResultFound as err:
            return {"message":"No existe el usuario que se desea eliminar"},404  
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
    
class UsuarioControllerById(Resource):
    @jwt_required()
    def get(self, idusuario):
        try:
            usuariodb = UsuarioModel.query.where(UsuarioModel.IDUSUARIO == idusuario).one()
            
            return UsuarioSchema().dump(usuariodb), 200
        
        except NoResultFound as err:
            return {"message":"No existe el usuario indicado"},404  
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503
        
#LOGIN
class UsuarioControllerLogin(Resource):
    def post(self):
        try:
            usuario = UsuarioSchemaLogin().load(request.json)
            
            usuariodb = UsuarioModel.query.where(
                UsuarioModel.CORREO == usuario["CORREO"]).where(
                UsuarioModel.CONTRASENIA == usuario["CONTRASENIA"]).one()
            
            usuario_schema = UsuarioSchema(exclude=["CONTRASENIA",]).dump(usuariodb)
            access_token = create_access_token(identity=usuario_schema, expires_delta=datetime.timedelta(days=1))
            
            return access_token, 200
        
        except NoResultFound as err:
            return {"message":"Correo o contrasenia equivocados."},404  
        except ValidationError as e:
            return e.messages, 422
        except Exception as e:
            return {"message": f"Algo salio mal, intenta de nuevo. {e}"}, 503            