from flask import Flask, Response, request, jsonify

from eat_it.controllers import AddUserController, AddUserRequest
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
def get_users() -> Response:
    user = request.json
    print(user)
    # repository = UserRepository()
    # controller = AddUserController(repository=repository)
    # add_user_request = AddUserRequest(user=user)
    # controller.add(request=add_user_request)
    return jsonify(user), 501


# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201
@app.post('/users/post')
def post_users() -> Response:
    user = request.json
    # repository = UserRepository()
    # controller = AddUserController(repository=repository)
    # add_user_request = AddUserRequest(user=user)
    # controller.add(request=add_user_request)
    return jsonify(user), 201


# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
@app.put('/users/put/<id>')
def put_users(id: int) -> Response:
    user = request.json
    # repository = UserRepository()
    # controller = AddUserController(repository=repository)
    # add_user_request = AddUserRequest(user=user)
    # controller.add(request=add_user_request)
    return jsonify(user), 200


# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200 (ponieważ PATCH powinien modyfikować jedynie częściowo - proszę przesłać JSON-a z tylko jednym kluczem)
@app.patch('/users/patch/<id>')
def patch_users(id: int) -> Response:
    user = request.json
    # repository = UserRepository()
    # controller = AddUserController(repository=repository)
    # add_user_request = AddUserRequest(user=user)
    # controller.add(request=add_user_request)
    return jsonify(user), 200


# 5. DELETE /users/<id> => zwraca 204
@app.delete('/users/delete/<id>')
def delete_users(id: int) -> Response:
    user = request.json
    # repository = UserRepository()
    # controller = AddUserController(repository=repository)
    # add_user_request = AddUserRequest(user=user)
    # controller.add(request=add_user_request)
    return jsonify(user), 204
