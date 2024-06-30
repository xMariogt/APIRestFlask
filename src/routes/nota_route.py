from src.controllers.nota_controller import NotaController, NotaControllerById
from flask_restx import Namespace

def NotaRoute(api):
    
    ns_nota = Namespace('nota', description='Endpoints de Notas')
    
    #hhtp://localhost:5000/ns_nota/v1/nota
    
    #Controlador para OBTENER, ACTUALIZAR Y CREAR NOTAS
    ns_nota.add_resource(NotaController, '')
    
    #Controlador que OBTIENE Y ELIMINA una nota por id
    ns_nota.add_resource(NotaControllerById, '/idnota/<int:idnota>')
    
    api.add_namespace(ns_nota)