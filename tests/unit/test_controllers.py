import json
from unittest.mock import Mock

import pytest
from _pytest.capture import CaptureFixture

from eat_it.controllers import AddUserController, GetUserController, PostUserController, PutUserController, PatchUserController, DeleteUserController
from eat_it.controllers import AddUserRequest, GetUserRequest, PostUserRequest, PutUserRequest, PatchUserRequest, DeleteUserRequest
from eat_it.repositories import UserRepository

@pytest.fixture
def payload() -> dict:
    return {"first_name": "Jan", "last_name": "Kowalski"}


@pytest.fixture
def user_repository() -> UserRepository:
    return Mock(UserRepository)

@pytest.fixture
def controller(user_repository: UserRepository) -> AddUserController:
    return AddUserController(repository=user_repository)

@pytest.fixture
def controller_get(user_repository: UserRepository) -> GetUserController:
    return GetUserController(repository=user_repository)

@pytest.fixture
def controller_post(user_repository: UserRepository) -> PostUserController:
    return PostUserController(repository=user_repository)

@pytest.fixture
def controller_put(user_repository: UserRepository) -> PutUserController:
    return PutUserController(repository=user_repository)

@pytest.fixture
def controller_patch(user_repository: UserRepository) -> PatchUserController:
    return PatchUserController(repository=user_repository)

@pytest.fixture
def controller_delete(user_repository: UserRepository) -> DeleteUserController:
    return DeleteUserController(repository=user_repository)


def test_add_user_controller_has_add_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: AddUserController,
) -> None:
    request = AddUserRequest(user=payload)
    controller.add(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

# PRACA DOMOWA
# 1. GET /users => zwraca 501
def test_get_user_controller_has_get_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: GetUserController,
) -> None:
    request = GetUserRequest()
    controller.get(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201
def test_post_user_controller_has_post_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: PostUserController,
) -> None:
    request = PostUserRequest(user=payload)
    controller.post(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
def test_put_user_controller_has_put_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: PutUserController,
) -> None:
    request = PutUserRequest(user=payload)
    controller.put(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
def test_patch_user_controller_has_patch_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: PatchUserController,
) -> None:
    request = PatchUserRequest(user=payload)
    controller.patch(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected

# 5. DELETE /users/<id> => zwraca 204
def test_delete_user_controller_has_delete_method(
    capsys: CaptureFixture,
    payload: dict,
    controller: DeleteUserController,
) -> None:
    request = DeleteUserRequest()
    controller.delete(request)
    actual = capsys.readouterr().out
    expected = f"{json.dumps(payload)}\n".replace('"', "'")
    assert actual == expected
    

# def test_calls_add_in_repository_on_calling_controller(
#         controller: AddUserController,
#         user_repository: Mock,
#         payload: dict,
# ) -> None:
#     request = AddUserRequest(user=payload)
#     controller.add(request)
#     user_repository.add.assert_called_once_with(payload)
#     assert user_repository.add.call_count == 0

# def test_add_user_request_has_user_attribute(payload: dict) -> None:
#     request = AddUserRequest(user=payload)
#     assert request.user

# def test_add_user_request_has_user_attribute_with_correct_type(payload: dict) -> None:
#     request = AddUserRequest(user=payload)
#     assert isinstance(request.user, dict)