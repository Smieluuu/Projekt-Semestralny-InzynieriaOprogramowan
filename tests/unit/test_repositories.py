import pytest
from eat_it.repositories import UserRepository

@pytest.fixture
def repository() -> UserRepository:
    return UserRepository()

def test_can_instantiate_user_repository(repository: UserRepository) -> None:
    assert isinstance(repository, UserRepository)

def test_raises_on_add_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.add()

def test_raises_on_get_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.get()

def test_raises_on_delete_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.delete()

def test_raises_on_post_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.post()

def test_raises_on_put_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.put()

def test_raises_on_patch_method(repository: UserRepository) -> None:
    with pytest.raises(NotImplementedError):
        repository.patch()
