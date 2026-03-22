# File to setup master.db
# Note: This master.db will be within logo_launch.

import sqlite3
import os

# Connecting to master.db thats within this folder
dbpath = os.path.join(os.path.dirname(__file__), 'master.db')
conn = sqlite3.connect(dbpath)
cursor = conn.cursor()

# Create tables if they don't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY AUTOINCREMENT,
    team_name TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS team_members (
    team_id INTEGER,
    user_id INTEGER,
    FOREIGN KEY(team_id) REFERENCES teams(team_id),
    FOREIGN KEY(user_id) REFERENCES users(user_id)
)
""")

# Commit changes and close connection
conn.commit()
conn.close()