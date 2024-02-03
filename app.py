
from flask import Flask, jsonify, request
from models.task import Task

app = Flask(__name__)

#CRUD
TASKS = []
task_count = 0

@app.route('/tasks', methods=['POST'])
def create_task():
  global task_count
  data = request.get_json()
  
  task = Task(id=task_count, title=data['title'], description=data['description'])
  task_count += 1
  
  TASKS.append(task)
  return jsonify({ 'message': 'Task created successfully!', 'task': task.to_dict() })

@app.route('/tasks', methods=['GET'])
def get_tasks():
  return jsonify({ 'tasks': [task.to_dict() for task in TASKS] })

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
  task = next((task for task in TASKS if task.id == task_id), None)
  if task:
    return jsonify({ 'task': task.to_dict() })
  return jsonify({ 'message': 'Task not found!' }), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
  data = request.get_json()
  task = next((task for task in TASKS if task.id == task_id), None)
  if task:
    task.title = data['title']
    task.description = data['description'] 
    task.done = data['done']
    return jsonify({ 'message': 'Task updated successfully!', 'task': task.to_dict() })
  return jsonify({ 'message': 'Task not found!' }), 404

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
  global TASKS
  TASKS = [task for task in TASKS if task.id != task_id]
  return jsonify({ 'message': 'Task deleted successfully!' })

if __name__ == '__main__':
  app.run(debug=True)