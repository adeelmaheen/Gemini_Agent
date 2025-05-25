# import sqlite3
# from datetime import datetime

# DB_FILE = "gemini_agent_memory.db"

# def get_connection():
#     return sqlite3.connect(DB_FILE, check_same_thread=False)

# def create_tables():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS chats (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 sender TEXT,
#                 message TEXT,
#                 timestamp TEXT
#             )
#         ''')
#         cursor.execute('''
#             CREATE TABLE IF NOT EXISTS notes (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 note TEXT,
#                 timestamp TEXT
#             )
#         ''')
#         conn.commit()

# def save_chat(sender, message):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(
#             "INSERT INTO chats (sender, message, timestamp) VALUES (?, ?, ?)",
#             (sender, message, datetime.now().isoformat())
#         )
#         conn.commit()

# def load_chats():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT sender, message FROM chats ORDER BY id")
#         rows = cursor.fetchall()
#     return rows

# def clear_chats():
#     """Clear all chat history from database."""
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM chats")
#         conn.commit()

# def save_note(note):
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute(
#             "INSERT INTO notes (note, timestamp) VALUES (?, ?)",
#             (note, datetime.now().isoformat())
#         )
#         conn.commit()

# def load_notes():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT note FROM notes ORDER BY id")
#         rows = cursor.fetchall()
#     return [row[0] for row in rows]

# def clear_notes():
#     with get_connection() as conn:
#         cursor = conn.cursor()
#         cursor.execute("DELETE FROM notes")
#         conn.commit()

import sqlite3

# Connect to SQLite DB
conn = sqlite3.connect("gemini_agent.db", check_same_thread=False)
cursor = conn.cursor()

# Create tables
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chats (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            sender TEXT,
            message TEXT
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT
        )
    ''')
    conn.commit()

# Chat Functions
def save_chat(sender, message):
    cursor.execute("INSERT INTO chats (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()

def load_chats():
    cursor.execute("SELECT sender, message FROM chats")
    return cursor.fetchall()

def clear_chats():
    cursor.execute("DELETE FROM chats")
    conn.commit()

# Notes Functions
def save_note(content):
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()

def load_notes():
    cursor.execute("SELECT content FROM notes")
    return [row[0] for row in cursor.fetchall()]

def clear_notes():
    cursor.execute("DELETE FROM notes")
    conn.commit()
