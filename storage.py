import sqlite3

def get_connection():
    return sqlite3.connect("app.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            email TEXT,
            hashed_password TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_user(user):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, hashed_password) VALUES (?, ?)", (user.email, user.hashed_password))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return new_id

def get_user_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    conn.close()
    return row