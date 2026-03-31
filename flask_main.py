# This is the main module for everything in this server.
# This handles all master I/O for the event backend.

# The following are all built-in modules:
from flask import Flask, request, jsonify
from flask_cors import CORS
import os

# The following are all user-defined modules:
from teams_creation import create_team
from login import team_login
from score import team_score
from leaderboard import leaderboards
from admin import get_users, set_quiz_status, get_status

# Defining the main Flask app:
app = Flask(__name__)
CORS(app)

# Defining default port to be $PORT env variable. Fallback to 5000 incase $PORT is unavailable.
port = int(os.environ.get("PORT", 5000))

# Creating Teams Module:
@app.route('/api/auth/register', methods=['POST'])
def teams_create():
    # Receive JSON Payload:
    payload = request.get_json()
    
    # Call the module:
    result = create_team(payload)

    # Return the result:
    return jsonify(result)

# Login Module:
@app.route('/api/auth/login', methods=['POST'])
def login():
    payload = request.get_json()
    result = team_login(payload)
    status_code = 200 if result.get("success") else 401
    return jsonify(result), status_code

# Commenting this out for now. Implementing admin module's actual quiz config
"""
# Event Status Module:
@app.route('/api/quiz/status', methods=['GET'])
def status():
    payload = { "enabled": True } # This is a bool value
    return jsonify(payload)
"""

"""
@app.route('/api/quiz/status', methods=['GET'])
def status():
    return jsonify(get_status())
"""

# Will make this shit tomorrow I guess.
# New Quiz Toggle thing
@app.route('/api/admin/quiz-status', methods=['POST'])
def toggle():
    payload = request.get_json()
    enabled = payload.get("enabled", False)
    result = set_quiz_status(enabled)
    return jsonify(result)

# Score Module:
@app.route('/api/quiz/score', methods=['POST'])
def score():
    payload = request.get_json()
    result = team_score(payload)
    return jsonify(result)

# Leaderboards Module:
@app.route('/api/leaderboard', methods=['GET'])
def leaderboard_main():
    result = leaderboards()
    return jsonify(result)

# Admin Module:
@app.route('/api/admin/users', methods=['GET'])
def admin_users():
    result = get_users()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug = True)