import pytest

from eat_it.repositories import UserRepository


@pytest.fixture
def repository() -> UserRepository:
    return UserRepository()


def test_can_instantiate_user_repository(
    repository: UserRepository,
) -> None:
    pass


def test_raises_on_add_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.add()


# PRACA DOMOWA 
# 1. GET /users => zwraca 501

# def test_get_users(repository: UserRepository) -> None:
#     with pytest.raises(NotImplementedError):
#         repository.get()


# # 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201

# def test_post_users(repository: UserRepository) -> None:
#     with pytest.raises(NotImplementedError):
#         repository.post()

# # 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

# def test_put_users(repository: UserRepository) -> None:
#     with pytest.raises(NotImplementedError):
#         repository.put()

# # 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

# def test_patch_users(repository: UserRepository) -> None:
#     with pytest.raises(NotImplementedError):
#         repository.patch()

# # 5. DELETE /users/<id> => zwraca 204

# def test_delete_users(repository: UserRepository) -> None:
#     with pytest.raises(NotImplementedError):
#         repository.delete()

        