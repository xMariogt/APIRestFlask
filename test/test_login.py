from app import app


#Happy Path
def test_login():
    client = app.test_client()
    
    response = client.post("/api/v1/login", json={
            "CORREO": "admin@gmail.com",
            "CONTRASENIA": "admin"
            })
    
    assert response.status_code == 200


#Sad Path