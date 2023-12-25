from datetime import datetime
from flask import Flask, request, jsonify
from main import app

users = {}
categories = {}
records = {}

@app.route('/healthcheck', methods=['GET'])
def health_check():
    service_status = 200
    date = datetime.utcnow().isoformat()

    response_data = {
        "date": date,
        "status": service_status
    }

    return jsonify(response_data), service_status

@app.route('/user/<user_id>', methods=['GET', 'DELETE'])
def get_or_delete_user(user_id):
    if request.method == 'GET':
        user = users.get(user_id)
        if user:
            return jsonify({'id': user['id'], 'name': user['name']})
        else:
            return jsonify({'error': 'User not found'}), 404
    elif request.method == 'DELETE':
        if user_id in users:
            del users[user_id]
            return jsonify({'message': 'User deleted successfully'})
        else:
            return jsonify({'error': 'User not found'}), 404

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    user_id = str(len(users) + 1)
    users[user_id] = {'id': user_id, 'name': data['name']}
    return jsonify({'id': user_id, 'name': data['name']})

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify([{'id': user['id'], 'name': user['name']} for user in users.values()])

@app.route('/category', methods=['POST', 'DELETE'])
def create_or_delete_category():
    if request.method == 'POST':
        data = request.get_json()
        category_id = str(len(categories) + 1)
        categories[category_id] = {'id': category_id, 'name': data['name']}
        return jsonify({'id': category_id, 'name': data['name']})
    elif request.method == 'DELETE':
        category_id = request.args.get('category_id')
        if category_id in categories:
            del categories[category_id]
            return jsonify({'message': 'Category deleted successfully'})
        else:
            return jsonify({'error': 'Category not found'}), 404

@app.route('/categories', methods=['GET'])
def get_categories():
    return jsonify([{'id': category['id'], 'name': category['name']} for category in categories.values()])

@app.route('/record/<record_id>', methods=['GET', 'DELETE'])
def get_or_delete_record(record_id):
    if request.method == 'GET':
        record = records.get(record_id)
        if record:
            return jsonify({
                'id': record['id'],
                'user_id': record['user_id'],
                'category_id': record['category_id'],
                'amount': record['amount']
            })
        else:
            return jsonify({'error': 'Record not found'}), 404
    elif request.method == 'DELETE':
        if record_id in records:
            del records[record_id]
            return jsonify({'message': 'Record deleted successfully'})
        else:
            return jsonify({'error': 'Record not found'}), 404

@app.route('/record', methods=['POST'])
def create_record():
    data = request.get_json()
    record_id = str(len(records) + 1)
    records[record_id] = {
        'id': record_id,
        'user_id': data['user_id'],
        'category_id': data['category_id'],
        'amount': data['amount']
    }
    return jsonify({
        'id': record_id,
        'user_id': data['user_id'],
        'category_id': data['category_id'],
        'amount': data['amount']
    })

@app.route('/records', methods=['GET'])
def get_records():
    user_id = request.args.get('user_id')
    category_id = request.args.get('category_id')

    filtered_records = []

    for record in records.values():
        user_condition = not user_id or record['user_id'] == user_id
        category_condition = not category_id or record['category_id'] == category_id

        if user_condition and category_condition:
            filtered_records.append(record)

    return jsonify({'records': filtered_records})

if __name__ == '__main__':
    app.run(debug=True)
