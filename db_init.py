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
        cid INTEGER,
        id INTEGER,
        name TEXT,
        course1 TEXT,
        course2 TEXT,
        course3 TEXT,
        marks1 INTEGER ,
        marks2 INTEGER ,
        marks3 INTEGER ,
        grade1 TEXT,
        grade2 TEXT,
        grade3 TEXT
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

    cur.execute("""
    CREATE TABLE IF NOT EXISTS gpa (
        cid INTEGER PRIMARY KEY AUTOINCREMENT,
        id INTEGER,
        credit_hours INTEGER,
        grade TEXT,
        grade_points REAL,
        gpa BOOLEAN
    )
    """)

    cur.execute('''CREATE TABLE IF NOT EXISTS Courses (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      course_name TEXT NOT NULL)''')

    
    cur.execute('''CREATE TABLE IF NOT EXISTS Classes (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      class_name TEXT NOT NULL,
                      course_id INTEGER,
                      teacher_name TEXT NOT NULL,
                      credit_hours INTEGER,
                      charges REAL,
                      description TEXT,
                      FOREIGN KEY (course_id) REFERENCES Courses (id))''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Students (
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
                        password TEXT)''')
    
    cur.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      student_id INTEGER,
                      class_id INTEGER,
                      FOREIGN KEY (student_id) REFERENCES Students (id),
                      FOREIGN KEY (class_id) REFERENCES Classes (id))''')


    con.commit()
    con.close()

create_db()
