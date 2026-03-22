# This is for creating a team for the event
# Endpoint Details:
"""
Type: POST
Endpoint: /api/auth/register
"""
import sqlite3
import os
"""
JSON Payload Example:
{
  "teamName":       "Quantum Wolves",
  "leaderUsername": "qwolf_lead",
  "password":       "plaintext123",   // backend hashes with bcrypt
  "members":        ["Alice", "Bob"]  // optional, can be empty array
}

"""

def create_team(payload):
    # Path to DB
    db_path = os.path.join(os.path.dirname(__file__), 'master.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Defining environment variables
    team_name = payload['teamName']
    leader = payload['leaderUsername']
    password = payload['password']
    members = payload['members']


    # Check if team exists
    cursor.execute("SELECT team_id FROM teams WHERE team_name = ?", (team_name,))
    result = cursor.fetchone()
    if result:
        conn.close()
        return {"status": "error", "message": "Team already exists"}

    # Insert team
    cursor.execute("INSERT INTO teams (team_name) VALUES (?)", (team_name,))
    team_id = cursor.lastrowid

    # Insert users and link to team
    for username in members:
        cursor.execute("SELECT user_id FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        if user:
            user_id = user[0]
        else:
            cursor.execute("INSERT INTO users (username) VALUES (?)", (username,))
            user_id = cursor.lastrowid
        cursor.execute("INSERT INTO team_members (team_id, user_id) VALUES (?, ?)", (team_id, user_id))

    conn.commit()
    conn.close()

    return {"status": "success", "team_id": team_id, "team_name": team_name}