# This is the 2nd iteration of team_create. I need to start from scratch, as that module is getting increasingly convoluted.
# Endpoint: /api/auth/register
# JSON Payload Example:
# {
#  "teamName":       "Quantum Wolves",
#  "leaderUsername": "qwolf_lead",
#  "password":       "plaintext123",
#  "members":        ["Alice", "Bob"]
# }
import sqlite3
import os
# Based on database schema, there's 3 things to do.
# Insert data into `teams`, `users`, and `members`
# Also, `members` as a name is shit af (can be confused with users??). This is a relation between users and teams bruh.
# So I'll make 3 functions: insert_teams, insert_users, and insert_members. They do this: insert into teams, users and members respectively.
# All the functions will use the same cursor. I'll call that before everything else so it exists within the module as a whole.

def cursorcall():
    pathofdb = os.path.join(os.path.dirname(__file__), 'master.db')
    conn = sqlite3.connect(pathofdb)
    conn.execute("PRAGMA foreign_keys = ON") # Better for SQLite since there are a lot of Foreign Keys
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    return conn, cursor

def insert_teams(cursor, payload):
    cursor.execute("INSERT INTO teams (team_name) VALUES (?)", (payload['teamName'],))
    teamid = cursor.lastrowid
    return teamid

def insert_users(cursor, payload, teamid):
    # Empty list for the user IDs, which is needed in `scores` table for the quiz.
    user_ids = []
    # First, inserting leader.
    cursor.execute("INSERT INTO users (username, password_hash, team_id, role) VALUES (?, ?, ?, ?)", (payload['leaderUsername'], payload['password'], teamid, 'leader'))
    user_ids.append(cursor.lastrowid)
    # Now leader is there in the db.
    # Inserting other users now.
    # Leader only has the password.
    # Members have none. In DB, it'll be NULL, passed by Python's None.
    for username in payload['members']:
        cursor.execute("INSERT INTO users (username, password_hash, team_id) VALUES (?, ?, ?)", (username, None, teamid))
        user_ids.append(cursor.lastrowid)
    return user_ids

def insert_members(cursor, all_team_members, teamid):
    member_ids = []
    for name in all_team_members:
        cursor.execute("INSERT INTO members (name, team_id) VALUES (?, ?)", (name, teamid))
        member_ids.append(cursor.lastrowid)
    return member_ids


def create_team(payload):
    conn, cursor = cursorcall()
    teamid = insert_teams(cursor, payload)
    user_ids = insert_users(cursor, payload, teamid)
    all_team_members = [payload['leaderUsername']] + payload['members']
    member_ids = insert_members(cursor, all_team_members, teamid)
    conn.commit()
    conn.close()