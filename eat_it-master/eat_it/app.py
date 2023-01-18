from flask import Flask, Response, request, jsonify

app = Flask(__name__)


@app.get("/ping")
def ping():
    return Response(status=501)


# 1. GET /users => zwraca 501
@app.get('/users', methods=['GET'])
def get_users() -> Response:
    return Response(status=501)

# 2. POST /users => zwraca przesłanego JSON-a i kod odpowiedzi 201
@app.rounte('/users', methods=['POST'])
def create_user() -> Response:
    user = request.json
    return jsonify(user), 201

# 3. PUT /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    data = request.get_json()
    return jsonify(data), 200

# 4. PATCH /users/<id> => zwraca przesłanego JSON-a i kod odpowiedzi 200 (ponieważ PATCH powinien modyfikować jedynie częściowo - proszę przesłać JSON-a z tylko jednym kluczem)
@app.route("/users/<id>", methods=["PATCH"])
def update_user_partial(id):
    data = request.get_json()
    return jsonify(data), 200

# 5. DELETE /users/<id> => zwraca 204
@app.route("/users/<id>", methods=["DELETE"])
def delete_user(id):
    return '', 204



