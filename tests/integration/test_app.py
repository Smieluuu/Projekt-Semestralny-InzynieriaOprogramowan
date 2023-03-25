from eat_it.app import app

UNIMPLEMENTED = 501


def test_app_has_ping_endpoint() -> None:
    client = app.test_client()
    response = client.get(path="/ping")
    assert response.status_code == UNIMPLEMENTED


def test_app_user_create_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users', json=payload)
    assert response.status_code == 200

# PRACA DOMOWA
# 1. GET /users => zwraca 501

def test_app_user_get_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.get(path='/users/get', json=payload)
    assert response.status_code == 501

# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201

def test_app_user_post_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.post(path='/users/post', json=payload)
    assert response.status_code == 201

# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

def test_app_user_put_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.put(path='/users/put/<id>', json=payload)
    assert response.status_code == 200

# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

def test_app_user_patch_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.patch(path=f'/users/patch/{1}', json=payload)
    assert response.status_code == 200

# 5. DELETE /users/<id> => zwraca 201

def test_app_user_delete_endpoint() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    client = app.test_client()
    response = client.delete(path=f'/users/delete/<{1}>', json=payload)
    assert response.status_code == 204
    