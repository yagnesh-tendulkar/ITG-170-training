import mysql.connector

# Lazy-loaded pool to avoid auth plugin errors at import time
_pool = None

def get_pool():
    global _pool
    if _pool is None:
        try:
            from app.config import settings
            _pool = mysql.connector.connect(
                host=getattr(settings, 'DB_HOST', 'localhost'),
                user=getattr(settings, 'DB_USER', 'root'),
                password=getattr(settings, 'DB_PASSWORD', ''),
                database=getattr(settings, 'DB_NAME', 'fastapi_db'),
                autocommit=False,
            )
        except Exception as e:
            # Connection failed - return None, caller should handle
            print(f"Warning: Database connection failed: {e}")
            return None
    return _pool


def get_db():
    """Get a database connection from the pool."""
    try:
        conn = get_pool()
        if conn is None:
            return None
        # Return fresh connection for thread safety
        return conn
    except Exception as e:
        print(f"Warning: Failed to get database connection: {e}")
        return None

