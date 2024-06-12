import sqlite3

def create_db():
    con = sqlite3.connect("GradeMaster.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id TEXT PRIMARY KEY,
        password TEXT,
        role TEXT 
    )
    """)

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
        course1 TEXT,
        course2 TEXT,
        course3 TEXT,
        marks1 INTEGER ,
        marks2 INTEGER ,
        marks3 INTEGER ,
        grade1 TEXT,
        grade2 TEXT,
        grade3 TEXT,
        gpa TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        id INTEGER,
        name TEXT,
        email TEXT,
        contact TEXT,
        course TEXT,
        profile_picture BLOB
    )
    """)    

    con.commit()
    con.close()

create_db()
