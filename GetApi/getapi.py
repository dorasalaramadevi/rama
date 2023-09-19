from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load data from a JSON file
with open('data.json', 'r') as json_file:
    data = json.load(json_file)

# Define a route to retrieve JSON data
@app.route('/get_data', methods=['GET'])

def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
