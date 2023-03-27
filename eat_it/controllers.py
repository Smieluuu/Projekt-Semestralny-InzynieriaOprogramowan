from dataclasses import dataclass

from eat_it.repositories import UserRepository


@dataclass
class AddUserRequest:
    user: dict

@dataclass
class GetUserRequest:
    pass

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
    def __init__(self, repository: UserRepository.add) -> None:
        pass

    def add(self, request: AddUserRequest) -> None:
        print(request.user)


# PRACA DOMOWA
# 1. GET /users => zwraca 501

class GetUserController:
    def __init__(self, repository: UserRepository.get) -> None:
        pass

    def get(self, request: GetUserRequest) -> None:
        raise NotImplementedError()

# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201

class PostUserController:
    def __init__(self, repository: UserRepository.post) -> None:
        pass

    def post(self, request: PostUserRequest) -> None:
        raise NotImplementedError()

# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

class PutUserController:
    def __init__(self, repository: UserRepository.put) -> None:
        pass

    def put(self, request: PutUserRequest) -> None:
        raise NotImplementedError()

# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200

class PatchUserController:
    def __init__(self, repository: UserRepository.patch) -> None:
        pass

    def patch(self, request: PatchUserRequest) -> None:
        raise NotImplementedError()

# 5. DELETE /users/<id> => zwraca 204

class DeleteUserController:
    def __init__(self, repository: UserRepository.delete) -> None:
        pass

    def delete(self, request: DeleteUserRequest) -> None:
        raise NotImplementedError()