from .nota_route import NotaRoute
from .usuario_route import UsuarioRoute
from .comentario_route import ComentarioRoute

def Routes(api):
    NotaRoute(api)
    UsuarioRoute(api)
    ComentarioRoute(api)