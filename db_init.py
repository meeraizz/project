import sqlite3

def create_db():
    con = sqlite3.connect("GradeMaster.db")
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
    
    cur.execute("""
    CREATE TABLE IF NOT EXISTS grade (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        id TEXT,
        name TEXT,
        course TEXT,
        marks_obt TEXT,
        full_marks TEXT,
        per TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        tid INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        contact TEXT,
        course TEXT
        profile_picture TEXT
    )
    """)



    

    con.commit()
    con.close()

create_db()
