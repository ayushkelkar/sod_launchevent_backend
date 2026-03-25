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
    cursor = conn.cursor()
    return conn, cursor

def insert_teams(cursor, payload):
    cursor.execute("INSERT INTO teams (team_name) VALUES (?)", (payload['teamName'],))
    teamid = cursor.lastrowid
    return teamid

def insert_users(cursor, payload):
    cursor.execute("INSERT INTO users (username, password_hash, team_id, )")

def create_team(payload):
    conn, cursor = cursorcall()
    insert_teams(cursor, payload)