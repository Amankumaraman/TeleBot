import sqlite3
import uuid

DATABASE = "database.db"

def init_db():
    """Initialize the database, creating necessary tables."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS UserLink (
            uuid TEXT PRIMARY KEY,
            telegram_id INTEGER NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_user_link(telegram_id, user_uuid):
    """Insert a new user link (UUID -> Telegram ID) into the database."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO UserLink (uuid, telegram_id) VALUES (?, ?)", (user_uuid, telegram_id))
    conn.commit()
    conn.close()

def get_user_id_by_uuid(user_uuid):
    """Retrieve the Telegram user ID for a given UUID."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT telegram_id FROM UserLink WHERE uuid = ?", (user_uuid,))
    result = cursor.fetchone()
    conn.close()
    return result
