import requests
import pytest

BASE_URL = "http://127.0.0.1:5000"

def test_create_task():
  response = requests.post(f'{BASE_URL}/tasks', json={
    'title': 'Test task',
    'description': 'Test description'
  })
  assert response.status_code == 200
  assert response.json() == {
    'message': 'Task created successfully!',
    'task': {
      'id': 0,
      "done": False,
      'title': 'Test task',
      'description': 'Test description'
    }
  }

def test_get_tasks():
  response = requests.get(f'{BASE_URL}/tasks')
  assert response.status_code == 200
  assert response.json() == {
    'tasks': [
      {
        'id': 0,
        'title': 'Test task',
        'description': 'Test description',
        "done": False,
      }
    ]
  }

def test_get_task():
  response = requests.get(f'{BASE_URL}/tasks/0')
  assert response.status_code == 200
  assert response.json() == {
    'task': {
      'id': 0,
      'title': 'Test task',
      'description': 'Test description',
      "done": False,
    }
  }

def test_update_task():
  response = requests.put(f'{BASE_URL}/tasks/0', json={
    'title': 'Updated task',
    'description': 'Updated description',
    'done': False
  })
  assert response.status_code == 200
  assert response.json() == {
    'message': 'Task updated successfully!',
    'task': {
      'id': 0,
      'title': 'Updated task',
      'description': 'Updated description',
      "done": False,
    }
  }

def test_delete_task():
  response = requests.delete(f'{BASE_URL}/tasks/0')
  assert response.status_code == 200
  assert response.json() == {
    'message': 'Task deleted successfully!'
  }