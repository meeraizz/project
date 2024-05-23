import sqlite3

# Function to create the database and course table
def create_db():
    con = sqlite3.connect(database="GradeMaster.db")
    cur = con.cursor()
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

# Function to insert data into the course table
def insert_course(name, duration, charges, description):
    con = sqlite3.connect(database="GradeMaster.db")
    cur = con.cursor()
    cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)", 
                (name, duration, charges, description))
    con.commit()
    con.close()

# Create the course table
create_db()

# Insert data into the course table
insert_course('Maths I', '3 months', 'RM300', 'Basic Maths')
insert_course('Physics I', '4 months', 'RM400', 'Basic Physics')
