from app.database import get_db

def create_tables():
    """Create tables if they don't exist. Gracefully handles no DB connection."""
    try:
        conn = get_db()
        if conn is None:
            print("Warning: Skipping table creation - no database connection")
            return
        
        cursor = conn.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            email VARCHAR(100) UNIQUE,
            password VARCHAR(255)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            priority VARCHAR(20),
            status VARCHAR(20) DEFAULT 'pending',
            user_id INT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)

        conn.commit()
        try:
            conn.close()
        except Exception:
            pass
    except Exception as e:
        print(f"Warning: Failed to create tables: {e}")
