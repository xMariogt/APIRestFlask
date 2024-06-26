from src.controllers.comentario_controller import (ComentarioController, ComentarioControllerPost, ComentarioControllerPut, 
    ComentarioControllerDelete, ComentarioControllerById)

def ComentarioRoute(api):
    api.add_resource(ComentarioController, '/comentarios')
    api.add_resource(ComentarioControllerPost, '/comentario')
    api.add_resource(ComentarioControllerPut, '/comentario')
    api.add_resource(ComentarioControllerDelete, '/comentario/idcomentario/<int:idcomentario>')
    api.add_resource(ComentarioControllerById, '/comentario/idcomentario/<int:idcomentario>')