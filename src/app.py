from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [{"label": "My first task", "done": False}]

# Rutas

@app.route("/home")  
def home():  
    return "Este es mi portafolio"  

@app.route("/about-me")  
def about_me():  
    return "Soy un desrrollador web en formación con 4Geeks academy" 

@app.route("/contact-me")  
def contact_me():  
    return "Mi correo electrónico es diegomenoruceta@gmail.com" 
    
@app.route("/todos", methods=['GET'])
def get_todos():  
    return jsonify(todos)

import json

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    new_todo = json.loads(request_body)
    todos.append(new_todo)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

print(request.data)