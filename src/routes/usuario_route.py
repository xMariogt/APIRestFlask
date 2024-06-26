from src.controllers.usuario_controller import UsuarioController, UsuarioControllerById, UsuarioControllerDelete, UsuarioControllerPost, UsuarioControllerPut

def UsuarioRoute(api):
    api.add_resource(UsuarioController, '/usuarios')
    api.add_resource(UsuarioControllerPost, '/usuario')
    api.add_resource(UsuarioControllerPut, '/usuario')
    api.add_resource(UsuarioControllerDelete, '/usuario/idusuario/<int:idusuario>')
    api.add_resource(UsuarioControllerById, '/usuario/idusuario/<int:idusuario>')