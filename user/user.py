import sqlite3

class User:
  def sign_up(username, password):
    conn = sqlite3.connect()
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO member VALUES 
    (?, ?, 'user')""")
    conn.commit()