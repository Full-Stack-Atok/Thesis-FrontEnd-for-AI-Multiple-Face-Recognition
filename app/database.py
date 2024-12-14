import sqlite3

def get_db():
  conn = sqlite3.connect('face_database.db')
  return conn

def create_table():
  conn = get_db()
  cursor = conn.cursor()
  cursor.execute('''
  CREATE TABLE IF NOT EXIST faces (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image BLOB NOT NULL
    )
  ''')
  conn.commit()
  conn.close()