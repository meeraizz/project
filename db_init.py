import sqlite3

def create_db():
    con = sqlite3.connect("GradeMaster.db")
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT,
        gender TEXT,
        dob TEXT,
        contact INTEGER,
        course TEXT,
        state TEXT,
        city TEXT,
        pin INTEGER,
        address TEXT,
        password TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS grade (
        id INTEGER,
        name TEXT,
        course TEXT,
        marks INTEGER ,
        grade TEXT,
        FOREIGN KEY (course) REFERENCES Courses (cid)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS teacher (
        id INTEGER,
        name TEXT,
        email TEXT,
        contact TEXT,
        course TEXT,
        profile_picture BLOB,
        password TEXT
    )
    """)    



    cur.execute('''CREATE TABLE IF NOT EXISTS Courses (
                      cid INTEGER PRIMARY KEY AUTOINCREMENT,
                      course_name TEXT,
                      credit_hour INTEGER,
                      charges TEXT,
                      description TEXT)''')

    

    

    
    cur.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_id INTEGER,
                      cid INTEGER,
                      FOREIGN KEY (student_id) REFERENCES student (id),
                      FOREIGN KEY (cid) REFERENCES Courses (cid))''')


    con.commit()
    con.close()

create_db()
