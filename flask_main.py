# This is the main module for everything in this server.
# This handles all master I/O for the backend.
# All I/O is in the form of JSONs
# For now I'm simulating team creation locally using Postman.

from flask import Flask, request, jsonify
from logo_launch.team_create import create_team

app = Flask(__name__)

@app.route('/api/auth/register', methods=['POST'])
def teams_create():
    # Get JSON payload from request
    payload = request.get_json()
    
    # Call the team creation function
    result = create_team(payload)
    
    # Return the result as JSON
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)