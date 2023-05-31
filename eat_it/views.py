from flask import Response, request, jsonify
from eat_it.controllers import (
    AddUserController, GetUserController, PostUserController,
    PutUserController, PatchUserController, DeleteUserController
)
from eat_it.controllers import (
    AddUserRequest, GetUserRequest, PostUserRequest,
    PutUserRequest, PatchUserRequest, DeleteUserRequest
)
from eat_it.repositories import UserRepository

class PingView:
    def get(self) -> Response:
        return Response(status=501)


class CreateUserView:
    def post(self) -> Response:
        user = request.json
        repository = UserRepository()
        controller = AddUserController(repository=repository)
        add_user_request = AddUserRequest(user=user)
        controller.add(request=add_user_request)
        return jsonify(user)


class GetUsersView:
    def get(self) -> Response:
        user = request.json
        repository = UserRepository()
        controller = GetUserController(repository=repository)
        try:
            get_user_request = GetUserRequest()
            controller.get(request=get_user_request)
        except NotImplementedError:
            return jsonify(user), 501
        return jsonify(user), 200


class PostUsersView:
    def post(self) -> Response:
        user = request.json
        repository = UserRepository()
        controller = PostUserController(repository=repository)
        try:
            post_user_request = PostUserRequest(user=user)
            controller.post(request=post_user_request)
        except NotImplementedError:
            print("no elo elo")
            return jsonify(user), 501
        return jsonify(user), 201


class PutUsersView:
    def put(self, id: int) -> Response:
        user = request.json
        repository = UserRepository()
        controller = PutUserController(repository=repository)
        try:
            put_user_request = PutUserRequest(user=user)
            controller.put(request=put_user_request)
        except NotImplementedError:
            return jsonify(user), 200
        return jsonify(user), 501


class PatchUsersView:
    def patch(self, id: int) -> Response:
        user = request.json
        repository = UserRepository()
        controller = PatchUserController(repository=repository)
        try:
            patch_user_request = PatchUserRequest(user=user)
            controller.patch(request=patch_user_request)
        except NotImplementedError:
            return jsonify(user), 200
        return jsonify(user), 501


class DeleteUsersView:
    def delete(self, id: int) -> Response:
        user = request.json
        repository = UserRepository()
        controller = DeleteUserController(repository=repository)
        try:
            delete_user_request = DeleteUserRequest(id=id)
            controller.delete(request=delete_user_request)
        except NotImplementedError:
            return jsonify(user), 204
        return jsonify(user), 501
