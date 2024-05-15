import sqlite3

def create_db():
    conn = sqlite3.connect(database="GradeMaster.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course (cid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, duration TEXT, charges TEXT, description TEXT)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student (roll INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, course TEXT)")
    conn.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result (rid INTEGER PRIMARY KEY AUTOINCREMENT, roll TEXT, name TEXT, course TEXT, marks_ob TEXT, full_marks TEXT, per TEXT)")
    conn.commit()

create_db()
