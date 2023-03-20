from fastapi.testclient import TestClient

from .main import app

client = TestClient(app)

error_404 = str("Animal not found")

def test_get_animal ():
    response = client.get("/view_register/Napo")
    assert response.status_code == 200
    assert response.json() == {
        "name" : "Napo",
        "species" : "Cat",
        "height" : 25.5,
        "age" : None,
        "weight" : None,
        "owner_name" : None,
        "day_of_register" : None
    }

def test_get_inexistent_animal ():
    response = client.get("/view_register/Duna")
    assert response.status_code == 404
    assert response.json() == {"detail": error_404}
    

def test_post_new_animal ():
    response =client.post("/new_register/", json = {
        "name" : "Duna",
        "species" : "Dog",
        "height" : None,
        "age" : 5,
        "weight" : None,
        "owner_name" : "Laura",
        "day_of_register" : None 
    })
    assert response.status_code == 200
    assert response.json () == {
        "name" : "Duna",
        "species" : "Dog",
        "height" : None,
        "age" : 5,
        "weight" : None,
        "owner_name" : "Laura",
        "day_of_register" : None 
    }


def test_post_invalid_animal ():
    response =client.post("/new_register/", json = {
        "name" : "Joan",
        "height" : None,
        "age" : 5,
        "weight" : None,
        "owner_name" : "Laura",
        "day_of_register" : None 
    })
    assert response.status_code == 422
    assert response.json() == {"detail": [{'loc': ['body', 'species'], 'msg': 'field required', 'type': 'value_error.missing'}]}


def test_update_animal ():
    response = client.put("/update_register/Parlanchin", json = {
        "name" : "Parlanchin",
        "species" : "Parrot",
        "height" : 45,
        "age" : 3,
        "weight" : None,
        "day_of_register" : 2022-9-15
    })


def test_update_invalid_animal ():
    response = client.put("/update_register/Enaitz", json = {        
        "species" : "Squirrel",
        "age" : None,
        "weight" : None,
        "owner_name" : None,
        "day_of_register" : None
        })
    assert response.status_code == 422

def test_update_inexistent_animal ():
    response = client.put("/update_register/Enaitz", json = {        
        "name" : "Enaitz",
        "species" : "Hedgehog",
        "height" : 25.5,
        "age" : None,
        "weight" : None,
        "owner_name" : None,
        "day_of_register" : None
        })
    assert response.status_code == 404
    assert response.json() == {"detail": error_404}

def test_delete_animal (): 
    response = client.delete("/delete/Yeti")
    assert response.status_code == 200
    assert response.json () == "Animal correctly deleted"

def test_delete_inexistent_animal ():
    response = client.delete("/delete/Mariona")
    assert response.status_code == 404
    assert response.json() == {"detail": error_404}


