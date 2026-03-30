from teams_creation import cursorcall

def toggle_quiz():
    conn, cursor = cursorcall()
    try:
        cursor.execute("SELECT enabled FROM quiz_config WHERE id = 1")
        row = cursor.fetchone()
        if row is None:
            cursor.execute("INSERT INTO quiz_config (id, enabled) VALUES (1, 1)")
            new_state = 1
        else:
            new_state = 0 if row["enabled"] else 1
            cursor.execute("UPDATE quiz_config SET enabled = ? WHERE id = 1", (new_state,))
        conn.commit()
        return {"success": True, "enabled": bool(new_state)}
    except Exception as e:
        conn.rollback()
        return {"success": False, "error": str(e)}
    finally:
        conn.close()

def get_status():
    conn, cursor = cursorcall()
    try:
        cursor.execute("SELECT enabled FROM quiz_config WHERE id = 1")
        row = cursor.fetchone()
        return {"enabled": bool(row["enabled"]) if row else False}
    except Exception as e:
        return {"enabled": False}
    finally:
        conn.close()

def get_users():
    conn, cursor = cursorcall()
    try:
        cursor.execute("""
            SELECT u.username, u.role, t.team_name
            FROM users u
            JOIN teams t ON u.team_id = t.id
            ORDER BY t.team_name, u.role DESC
        """)
        rows = cursor.fetchall()
        users = [
            {"username": row["username"], "role": row["role"], "teamName": row["team_name"]}
            for row in rows
        ]
        return {"success": True, "users": users}
    except Exception as e:
        return {"success": False, "users": [], "error": str(e)}
    finally:
        conn.close()