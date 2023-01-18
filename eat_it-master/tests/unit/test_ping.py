from eat_it.app import app, ping, get_users, create_user, update_user, update_user_partial, delete_user
from unittest.mock import patch

UNIMPLEMENTED = 501


def test_ping_returns_501_response() -> None:
    result = ping()
    assert result.status_code == UNIMPLEMENTED


def test_create_user_returns_user() -> None:
    payload = {"first_name": "Jan", "last_name": "Kowalski"}
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = create_user()
    assert result.json == payload


# 1. GET /users => zwraca 501
def test_get_users():
    result = get_users()

    assert result.status_code == 501


# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201
def test_create_user():
    user = {'name': 'John', 'age': 30}
    expected_status_code = 201

    with patch('flask.request') as mock_request:
        mock_request.json = user
        result = create_user()

    assert result.status_code == expected_status_code
    assert result.get_json() == user


# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
def test_update_user_partial():
    user_id = 1
    updated_user = {'name': 'Jane'}
    expected_status_code = 200

    with patch('flask.request') as mock_request:
        mock_request.json = updated_user
        result = update_user(user_id)

    assert result.status_code == expected_status_code
    assert result.get_json() == updated_user


# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200 (ponieważ PATCH powinien modyfikować jedynie częściowo - proszę przesłać JSON-a z tylko jednym kluczem)
def test_update_user_partial():
    user_id = 1
    updated_user = {'name': 'Jane'}
    expected_status_code = 200

    with patch('flask.request') as mock_request:
        mock_request.json = updated_user
        result = update_user_partial(user_id)

    assert result.status_code == expected_status_code
    assert result.get_json() == updated_user


# 5. DELETE /users/<id> => zwraca 204
def test_delete_user():
    user_id = 1
    expected_status_code = 204

    result = delete_user(user_id)

    assert result.status_code == expected_status_code
