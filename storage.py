import sqlite3

def get_connection():
    return sqlite3.connect("app.db")

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            email TEXT UNIQUE,
            hashed_password TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS medications (
            refill_id INTEGER PRIMARY KEY,
            user_id INTEGER,
            medication_name TEXT,
            dosage TEXT,
            instructions TEXT,
            last_refill_date TEXT,
            days_per_supply INTEGER,
            refills_remaining INTEGER,
            FOREIGN KEY (user_id) REFERENCES users(user_id)
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