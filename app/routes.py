from flask import Blueprint, request, jsonify
from .models import Task
from . import db

main = Blueprint('main', __name__)

@main.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{
        'id': task.id,
        'entity_name': task.entity_name,
        'task_type': task.task_type,
        'date': str(task.date),
        'time': str(task.time),
        'contact_person': task.contact_person,
        'note': task.note,
        'status': task.status
    } for task in tasks])

@main.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    new_task = Task(
        entity_name=data['entity_name'],
        task_type=data['task_type'],
        date=data['date'],
        time=data['time'],
        contact_person=data['contact_person'],
        note=data.get('note'),
        status=data['status']
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

@main.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    task = Task.query.get_or_404(task_id)
    task.entity_name = data.get('entity_name', task.entity_name)
    task.task_type = data.get('task_type', task.task_type)
    task.date = data.get('date', task.date)
    task.time = data.get('time', task.time)
    task.contact_person = data.get('contact_person', task.contact_person)
    task.note = data.get('note', task.note)
    task.status = data.get('status', task.status)
    db.session.commit()
    return jsonify({'message': 'Task updated successfully'})

@main.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({'message': 'Task deleted successfully'})
