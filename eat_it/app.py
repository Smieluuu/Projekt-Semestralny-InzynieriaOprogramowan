from flask import Flask, Response, request, jsonify

from eat_it.controllers import AddUserController, GetUserController, PostUserController, PutUserController, PatchUserController, DeleteUserController
from eat_it.controllers import AddUserRequest, GetUserRequest, PostUserRequest, PutUserRequest, PatchUserRequest, DeleteUserRequest
from eat_it.repositories import UserRepository

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


@app.post('/users')
def create_user() -> Response:
    user = request.json
    repository = UserRepository()
    controller = AddUserController(repository=repository)
    add_user_request = AddUserRequest(user=user)
    controller.add(request=add_user_request)
    return jsonify(user)


@app.put('/users')
def update_user() -> Response:
    user = request.json
    return jsonify(user)

# PRACA DOMOWA
# 1. GET /users => zwraca 501
@app.get('/users/get')
def get_users():
    user = request.json
    repository = UserRepository()
    controller = GetUserController(repository=repository)
    try:
        get_user_request = GetUserRequest()
        controller.get(request=get_user_request)
    except NotImplementedError:
        return jsonify(user), 501
    return jsonify(user), 200
    

# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201
@app.post('/users/post')
def post_users():
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
    

# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
@app.put('/users/put/<id>')
def put_users(id: int) -> Response:
    user = request.json
    repository = UserRepository()
    controller = PutUserController(repository=repository)
    try:
        put_user_request = PutUserRequest(user=user)
        controller.put(request=put_user_request)
    except NotImplementedError:
        return jsonify(user), 200
    return jsonify(user), 501


# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200 (ponieważ PATCH powinien modyfikować jedynie częściowo - proszę przesłać JSON-a z tylko jednym kluczem)
@app.patch('/users/patch/<int:id>')
def patch_users(id: int) -> Response:
    user = request.json
    repository = UserRepository()
    controller = PatchUserController(repository=repository)
    try:
        patch_user_request = PatchUserRequest(user=user)
        controller.patch(request=patch_user_request)
    except NotImplementedError:
        return jsonify(user), 200
    return jsonify(user), 501


# 5. DELETE /users/<id> => zwraca 204
@app.delete('/users/delete/<id>')
def delete_users(id: int) -> Response:
    user = request.json
    repository = UserRepository()
    controller = DeleteUserController(repository=repository)
    try:
        delete_user_request = DeleteUserRequest(id=id)
        controller.delete(request=delete_user_request)
    except NotImplementedError:
        return jsonify(user), 204
    return jsonify(user), 501
