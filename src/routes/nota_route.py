from src.controllers.nota_controller import NotaController, NotaControllerPost, NotaControllerPut, NotaControllerById, NotaControllerDelete
from flask_restx import Namespace

def NotaRoute(api):
    
    ns_nota = Namespace('nota', description='Endpoints de Notas')
    
    #hhtp://localhost:5000/api/v1/nota
    
    api.add_resource(NotaController, '/notas')
    api.add_resource(NotaControllerPost, '/nota')
    api.add_resource(NotaControllerPut, '/nota')
    api.add_resource(NotaControllerById, '/nota/idnota/<int:idnota>')
    api.add_resource(NotaControllerDelete, '/nota/idnota/<int:idnota>')