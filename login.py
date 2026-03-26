from teams_creation import cursorcall
import jwt
import datetime
# This module will handle the team login.
# Endpoint: /api/auth/login
# Type: POST
# JSON Payload Example:
# {
#   "username": "qwolf_lead",
#   "password": "plaintext123"
# }

# If Successful, should send the following payload:
# {
#   "token": "eyJhbGciOiJIUzI1NiJ9...",
#   "user": {
#   "id": 1,
#   "username": "qwolf_lead",
#   "teamName": "Quantum Wolves",   // camelCase — not team_name
#   "role":     "leader"
#           }
# }

# So login works with valid credentials. However, login with invalid credentials is messy, doesn't work right, and kind of weird. Will see later.

SECRET_KEY = "I don't know what the hell to put here"

def teams_check(cursor, username, password):
    cursor.execute("SELECT * FROM users WHERE username = ? AND password_hash = ?", (username, password))
    row = cursor.fetchone()
    if row == None:
        return None
    teamid = row["team_id"]
    cursor.execute("SELECT team_name FROM teams WHERE id = ?", (teamid,))
    teamsrow = cursor.fetchone()
    user_info = {
        "id": row["id"],
        "username": row["username"],
        "teamName": teamsrow["team_name"] if teamsrow else None,
        "role": row["role"]
        }
    return user_info

def jwtthing(payload):
    d1 = payload
    d1['exp'] = datetime.datetime.now() + datetime.timedelta(hours=2)
    token = jwt.encode(d1, SECRET_KEY, algorithm="HS256")
    return token

def team_login(payload):
    username = payload['username']
    password = payload['password']
    conn, cursor = cursorcall()
    user_info = teams_check(cursor, username, password)
    token = jwtthing(payload)
    if user_info == None:
        return {"message": "Invalid credentials"}
    response = {
        "token": token,
        "user": user_info
        }
    return response