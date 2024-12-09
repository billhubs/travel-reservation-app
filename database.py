import sqlite3

def create_database():
    conn = sqlite3.connect('app.db')
    c = conn.cursor()
    
    # Create reservations table
    c.execute('''CREATE TABLE IF NOT EXISTS reservations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL,
                    date TEXT NOT NULL)''')
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
