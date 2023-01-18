from eat_it.app import app

UNIMPLEMENTED = 501


def test_app_has_ping_endpoint() -> None:
    client = app.test_client()
    response = client.get(path="/ping")
    assert response.status_code == UNIMPLEMENTED


# 1. GET /users => zwraca 501
def test_get_users():
    client = app.test_client()
    response = client.get('/users')
    status_code = response.status_code

    assert status_code == UNIMPLEMENTED


# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201
def test_create_user():
    user = {'name': 'John', 'age': 30}
    expected_status_code = 201

    client = app.test_client()
    response = client.post('/users', json=user)
    status_code = response.status_code
    data = response.get_json()

    assert status_code == expected_status_code
    assert data == user


# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
def test_update_user():
    user_id = 1
    updated_user = {'name': 'Jane', 'age': 25}
    expected_status_code = 200

    client = app.test_client()
    response = client.put(f'/users/{user_id}', json=updated_user)
    status_code = response.status_code
    data = response.get_json()

    assert status_code == expected_status_code
    assert data == updated_user


# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200 (ponieważ PATCH powinien modyfikować jedynie częściowo - proszę przesłać JSON-a z tylko jednym kluczem)
def test_update_user_partial():
    user_id = 1
    updated_user = {'name': 'Jane'}
    expected_status_code = 200

    client = app.test_client()
    response = client.patch(f'/users/{user_id}', json=updated_user)
    status_code = response.status_code
    data = response.get_json()

    assert status_code == expected_status_code
    assert data == updated_user


# 5. DELETE /users/<id> => zwraca 204
def test_delete_user():
    user_id = 1
    expected_status_code = 204

    client = app.test_client()
    response = client.delete(f'/users/{user_id}')
    status_code = response.status_code

    assert status_code == expected_status_code
