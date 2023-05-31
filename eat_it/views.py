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
    def __init__(self, controller: AddUserController) -> None:
        self._controller = controller

    def post(self) -> Response:
        user = request.json
        add_user_request = AddUserRequest(user=user)
        self.controller.add(request=add_user_request)
        return jsonify(user)


class GetUsersView:
    def __init__(self, controller: GetUserController) -> None:
        self.controller = controller

    def get(self) -> Response:
        user = request.json
        get_user_request = GetUserRequest()
        try:
            self.controller.get(request=get_user_request)
        except NotImplementedError:
            return jsonify(user), 501
        return jsonify(user), 200


class PostUsersView:
    def __init__(self, controller: PostUserController) -> None:
        self.controller = controller

    def post(self) -> Response:
        user = request.json
        post_user_request = PostUserRequest(user=user)
        try:
            self.controller.post(request=post_user_request)
        except NotImplementedError:
            return jsonify(user), 501
        return jsonify(user), 201


class PutUsersView:
    def __init__(self, controller: PutUserController) -> None:
        self.controller = controller

    def put(self, id: int) -> Response:
        user = request.json
        put_user_request = PutUserRequest(user=user)
        try:
            self.controller.put(request=put_user_request)
        except NotImplementedError:
            return jsonify(user), 501
        return jsonify(user), 200


class PatchUsersView:
    def __init__(self, controller: PatchUserController) -> None:
        self.controller = controller

    def patch(self, id: int) -> Response:
        user = request.json
        patch_user_request = PatchUserRequest(user=user)
        try:
            self.controller.patch(request=patch_user_request)
        except NotImplementedError:
            return jsonify(user), 501
        return jsonify(user), 200


class DeleteUsersView:
    def __init__(self, controller: DeleteUserController) -> None:
        self.controller = controller

    def delete(self, id: int) -> Response:
        user = request.json
        delete_user_request = DeleteUserRequest(id=id)
        try:
            self.controller.delete(request=delete_user_request)
        except NotImplementedError:
            return jsonify(user), 501
        return jsonify(user), 204
