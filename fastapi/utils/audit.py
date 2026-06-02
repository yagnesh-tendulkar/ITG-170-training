from database.db import mydb, mycursor


def ensure_audit_table():
    query = """
    CREATE TABLE IF NOT EXISTS audit_logs (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        action TEXT NOT NULL,
        action_time DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """
    mycursor.execute(query)
    mydb.commit()


def log_action(username: str, action: str):
    """Insert an audit log entry. Creates table if missing."""
    try:
        ensure_audit_table()
        query = "INSERT INTO audit_logs (username, action) VALUES (%s, %s)"
        mycursor.execute(query, (username, action))
        mydb.commit()
        return {"id": mycursor.lastrowid, "username": username, "action": action}
    except Exception as e:
        # Don't break main flow if logging fails; optionally handle/report
        print("Audit log error:", e)
        return None
