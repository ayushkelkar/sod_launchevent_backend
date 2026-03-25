# This is the main module for everything in this server.
# This handles all master I/O for the backend.

from flask import Flask, request, jsonify
from logo_launch.teams_creation import create_team
from logo_launch.login import team_login
from logo_launch.score import team_score
from logo_launch.leaderboard import leaderboards
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# This is the create teams part:
@app.route('/api/auth/register', methods=['POST'])
def teams_create():
    # Get JSON payload from request
    payload = request.get_json()
    
    # Call the team creation function
    result = create_team(payload)

    # Return the result as JSON
    return jsonify(result)

# This is the login part:
@app.route('/api/auth/login', methods=['POST'])
def login():
    payload = request.get_json()
    result = team_login(payload)
    return jsonify(result)

# This is the event enabled status part:
@app.route('/api/quiz/status', methods=['GET'])
def status():
    payload = { "enabled": True } # This is a bool value
    return jsonify(payload)

# This is the score module
@app.route('/api/quiz/score', methods=['POST'])
def score():
    payload = request.get_json()
    result = team_score(payload)
    return jsonify(result)

# This is the leaderboards module
@app.route('/api/leaderboard', methods=['GET'])
def leaderboard_main():
    result = leaderboards()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)