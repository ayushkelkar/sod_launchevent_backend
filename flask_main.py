# This is the main module for everything in this server.
# This handles all master I/O for the backend.

from flask import Flask, request, jsonify
from logo_launch.teams_creation import create_team
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/auth/register', methods=['POST'])
def teams_create():
    # Get JSON payload from request
    payload = request.get_json()
    
    # Call the team creation function
    result = create_team(payload)

    # Return the result as JSON
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)