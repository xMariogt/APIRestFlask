

def test_nota(cliente, header):
    response = cliente.post("/api/v1/nota", json={
        "DESCRIPCION": "Este es mi primer NOTA",
        "FECHA": "2024-06-20T00:00:00",
        "IDUSUARIO": 1
        }, headers=header)
    
    assert response.status_code == 201
    #Para este se debe reiniciar la base de datos de prueba cada vez que se corra
    #Para que elimine todos los elementos y el IDNOTA sea 1
    #assert response.json["IDNOTA"] == 1
    
def test_notas(cliente, header):
    response = cliente.get("/api/v1/nota", headers=header)
    
    assert response.status_code == 200