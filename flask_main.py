# This is the main module for everything in this server.
# This handles all master I/O for the backend.
# All I/O is in the form of JSONs
# For now I'm simulating team creation locally using Postman.

from flask import Flask, request, jsonify
from logo_launch.team_create import create_team
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/auth/register', methods=['POST'])
def teams_create():
    # Get JSON payload from request
    payload = request.get_json()
    
    # Call the team creation function comment this shit I don't need this for now
    #result = create_team(payload)
    # print the goddamn payload so I understand wtf is being sent
    print(payload)
    # Return the result as JSON
    return jsonify(payload)

if __name__ == '__main__':
    app.run(debug=True)