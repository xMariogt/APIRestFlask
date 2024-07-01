import pytest
from app import app

#Este es el cliente para realizar las pruebas
@pytest.fixture()
def cliente():
    cliente = app.test_client()
    
    yield cliente

#Esto crea una consulta de prueba para el usuario admin y devuelve el token
#Lo que permite que se puedan realizar pruebas con las rutas protegidas
@pytest.fixture()
def header(cliente):
    response = cliente.post("/api/v1/login", json={
            "CORREO": "admin@gmail.com",
            "CONTRASENIA": "admin"
            })
    
    token = response.json['token']
    header = {"Authorization": f"Bearer {token}"}
    
    yield header