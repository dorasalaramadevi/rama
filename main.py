from flask import Flask, request, jsonify
from db_operations import get_employees, get_employee, add_employee, update_employee, delete_employee

app = Flask(__name__)


@app.route('/api/employees', methods=['GET'])
def get_all_employees():
    employees = get_employees()

    return jsonify(employees), 200


@app.route('/api/employees/<int:id>', methods=['GET'])
def get_single_employee(id):
    employee = get_employee(id)

    if employee:

        return jsonify(employee), 200

    else:

        return 'Employee not found', 404


@app.route('/api/employees', methods=['POST'])
def create_employee():
    data = request.get_json()

    name = data.get('name')

    department = data.get('department')

    if name and department:

        add_employee(name, department)

        return 'Employee added successfully', 201

    else:

        return 'Invalid JSON data format or missing fields', 400


@app.route('/api/employees/<int:id>', methods=['PUT'])
def update_single_employee(id):
    data = request.get_json()

    name = data.get('name')

    department = data.get('department')

    if name and department:

        update_employee(id, name, department)

        return 'Employee updated successfully', 200

    else:

        return 'Invalid JSON data format or missing fields', 400


@app.route('/api/employees/<int:id>', methods=['DELETE'])
def delete_single_employee(id):
    delete_employee(id)

    return 'Employee deleted successfully', 200


if __name__ == '__main__':
    app.run(debug=True)
