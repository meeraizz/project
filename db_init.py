import sqlite3

def create_db():
    con = sqlite3.connect("Grademaster.db")
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id TEXT PRIMARY KEY,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact TEXT,
        admission TEXT,
        course TEXT,
        state TEXT,
        city TEXT,
        pin TEXT,
        address TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS course (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT, 
        duration TEXT, 
        charges TEXT, 
        description TEXT
    )
    """)

    con.commit()
    con.close()

create_db()
