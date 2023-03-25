import json

import pytest

from eat_it.app import app
from eat_it.app import create_user
from eat_it.app import update_user


@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


def test_create_user_returns_user(payload: dict) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = create_user()
    assert result.json == payload


def test_create_user_prints_user_on_console(payload: dict, capsys) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        create_user()
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected


def test_update_user_returns_user(payload: dict) -> None:
    with app.test_request_context(method="PUT", path="/users", json=payload):
        result = update_user()
    assert result.json == payload


# PRACA DOMOWA
# 1. GET /users => zwraca 501

def test_get_user_returns_501() -> None:
    with app.test_request_context(method="GET", path="/users"):
        result = app.full_dispatch_request()
    assert result.status_code == 501

# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201

def test_post_user_returns_201(payload: dict) -> None:
    with app.test_request_context(method="POST", path="/users", json=payload):
        result = app.full_dispatch_request()
    assert result.status_code == 201


# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

def test_put_user_returns_200(payload: dict) -> None:
    with app.test_request_context(method="PUT", path="/users", json=payload):
        result = app.full_dispatch_request()
    assert result.status_code == 200


# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

def test_patch_user_returns_200(payload: dict) -> None:
    with app.test_request_context(method="PATCH", path="/users", json=payload):
        result = app.full_dispatch_request()
    assert result.status_code == 200


# 5. DELETE /users/<id> => zwraca 201

def test_delete_user_returns_204() -> None:
    with app.test_request_context(method="DELETE", path="/users", json=payload):
        result = app.full_dispatch_request()
    assert result.status_code == 204