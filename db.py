# import sqlite3

# # Connect to SQLite DB
# conn = sqlite3.connect("gemini_agent.db", check_same_thread=False)
# cursor = conn.cursor()

# # Create tables
# def create_tables():
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS chats (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             sender TEXT,
#             message TEXT
#         )
#     ''')
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS notes (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             content TEXT
#         )
#     ''')
#     conn.commit()

# # Chat Functions
# def save_chat(sender, message):
#     cursor.execute("INSERT INTO chats (sender, message) VALUES (?, ?)", (sender, message))
#     conn.commit()

# def load_chats():
#     cursor.execute("SELECT sender, message FROM chats")
#     return cursor.fetchall()

# def clear_chats():
#     cursor.execute("DELETE FROM chats")
#     conn.commit()

# # Notes Functions
# def save_note(content):
#     cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
#     conn.commit()

# def load_notes():
#     cursor.execute("SELECT content FROM notes")
#     return [row[0] for row in cursor.fetchall()]

# def clear_notes():
#     cursor.execute("DELETE FROM notes")
#     conn.commit()
import sqlite3
import os
import tempfile

# Use a writable directory for the database file (e.g., /tmp/)
db_path = os.path.join(tempfile.gettempdir(), "gemini_agent.db")

# Connect to the SQLite database
conn = sqlite3.connect(db_path, check_same_thread=False)
cursor = conn.cursor()

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

def save_chat(sender, message):
    cursor.execute("INSERT INTO chats (sender, message) VALUES (?, ?)", (sender, message))
    conn.commit()

def load_chats():
    cursor.execute("SELECT sender, message FROM chats ORDER BY id")
    return cursor.fetchall()

def clear_chats():
    cursor.execute("DELETE FROM chats")
    conn.commit()

def save_note(content):
    cursor.execute("INSERT INTO notes (content) VALUES (?)", (content,))
    conn.commit()

def load_notes():
    cursor.execute("SELECT content FROM notes ORDER BY id")
    return [row[0] for row in cursor.fetchall()]

def clear_notes():
    cursor.execute("DELETE FROM notes")
    conn.commit()
