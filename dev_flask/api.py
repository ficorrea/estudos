from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route('/home')
def home():
    return 'Home Page'

@app.route('/health')
def health():
    return jsonify({"status": "healthy"}), 200

tasks = []
task_id_control = 1  # Controlador de IDs para garantir unicidade

@app.route('/task', methods=['POST'])
def post_task():
    try:
        global task_id_control
        data = request.get_json()
        task = {
            'task_id': task_id_control,
            'tt_id': data.get('tt_id', None),
            'nome': data.get('nome', None)
        }
        tasks.append(task)
        task_id_control += 1
        return jsonify({'msg': 'Tarefa criada.', 'task': task}), 201
    except Exception as error:
        return jsonify({'msg': 'Erro ao criar tarefa.', 'erro': error}), 404

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({"tasks": tasks, "total": len(tasks)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)