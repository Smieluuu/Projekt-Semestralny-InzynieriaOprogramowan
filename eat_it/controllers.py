from dataclasses import dataclass
from eat_it.repositories import UserRepository

@dataclass
class AddUserRequest:
    user: dict

@dataclass
class GetUserRequest:
    id: int

@dataclass
class PostUserRequest:
    user: dict

@dataclass
class PutUserRequest:
    user: dict

@dataclass
class PatchUserRequest:
    user: dict

@dataclass
class DeleteUserRequest:
    id: int


class AddUserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def add(self, request: AddUserRequest) -> None:
        self.repository.add_user(request.user)


class GetUserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def get(self, request: GetUserRequest) -> dict:
        return self.repository.get_user(request.id)


class PostUserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def post(self, request: PostUserRequest) -> dict:
        return self.repository.create_user(request.user)


class PutUserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def put(self, request: PutUserRequest) -> dict:
        return self.repository.update_user(request.user)


class PatchUserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def patch(self, request: PatchUserRequest) -> dict:
        return self.repository.patch_user(request.user)


class DeleteUserController:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def delete(self, request: DeleteUserRequest) -> None:
        self.repository.delete_user(request.id)
