rom flask import Flask, jsonify, request

app = Flask(__name__)

todos = [ { "label": "My first task", "done": False } ]

# Ruta de ejemplo que devuelve un mensaje de bienvenida
@app.route('/todos', methods=['GET'])
def hello_todos():
    todos_text = jsonify(todos)
    return todos_text



@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos), 201


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("this is the position to delete", position)
    return (todos)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
