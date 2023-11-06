from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{ "label": "My first task", "done": False }]

@app.route('/myroute', methods=['GET'])
def hello_world():
    return 'Hello, World!'

#GET
@app.route('/todos', methods=['GET'])
def get_todos():
   json_todos = jsonify(todos)
   return json_todos

#POST
@app.route('/todos', methods=['POST'])
def add_new_todo():
    try:
        request_body = request.get_json(force=True)
        todos.append(request_body)  # Add the new todo to the todos list
        updated_todos = jsonify(todos)  # Convert the updated todos list to JSON
        return updated_todos
    except Exception as e:
        return jsonify(error=str(e)), 400  # Return error

#DELETE
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    
    todos.pop((position-1))
    
    return jsonify(todos)

# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)