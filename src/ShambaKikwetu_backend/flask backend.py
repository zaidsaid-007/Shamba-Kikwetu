from flask import Flask, request, jsonify
import requests
import jwt
from functools import wraps

app = Flask(__name__)


if __name__ == '__main__':
    app.run(debug=True)



# Define the base URL for your IC canisters
IC_BASE_URL = "https://ic0.app/api/v2/canister/YOUR_CANISTER_ID/"


users = {}  # Dictionary to store user data

# User registration endpoint
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    

    if username in users:
        return jsonify({'message': 'User already exists'}), 400

    users[username] = {'password': password}
    return jsonify({'message': 'User registered successfully'}), 201

# User login endpoint
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if username not in users or users[username]['password'] != password:
        return jsonify({'message': 'Invalid credentials'}), 401

    token = jwt.encode({'username': username}, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token.decode('utf-8')})


# API endpoint to list land ownership records 
@app.route("/api/land-records", methods=["GET"])
def get_land_records():
    try:
        response = requests.get(IC_BASE_URL + "getLandRecords")
        if response.status_code == 200:
            land_records = response.json()
            return jsonify(land_records), 200
        else:
            return jsonify({"error": "Failed to fetch land records"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# API endpoint to register a new land ownership record
@app.route("/api/register-land", methods=["POST"])
def register_land():
    try:
        data = request.get_json()
        owner = data.get("owner")
        land_details = data.get("land_details")
        land_id = data.get("land_id")

        payload = {
            "owner": owner,
            "landDetails": land_details,
            "landID": land_id
        }

        response = requests.post(IC_BASE_URL + "registerLand", json=payload)
        if response.status_code == 200:
            return jsonify({"message": "Land record registered successfully"}), 200
        else:
            return jsonify({"error": "Failed to register land record"}), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
