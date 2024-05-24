import sqlite3

# Function to create the database and course table
def create_db():
    con = sqlite3.connect(database="GradeMaster.db")
    cur = con.cursor()

    # Create the course table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course (
            cid INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT, 
            duration TEXT, 
            charges TEXT, 
            description TEXT
        )
    """)

    # Create the student table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student (
            roll INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT,
            gender TEXT,
            dob TEXT,
            contact TEXT,
            admission TEXT
        )
    """)

    # Create the result table
    cur.execute("""
        CREATE TABLE IF NOT EXISTS result (
            rid INTEGER PRIMARY KEY AUTOINCREMENT,
            roll TEXT,
            name TEXT,
            course TEXT,
            marks_obt TEXT,
            full_marks TEXT,
            per TEXT
        )
    """)



# Call the function to create the database and tables
create_db()



#Function to insert data into the course table
#def insert_course(name, duration, charges, description):
 #  cur = con.cursor()
 # cur.execute("INSERT INTO course (name, duration, charges, description) VALUES (?, ?, ?, ?)", 
   #             (name, duration, charges, description))
    #con.commit()
    #con.close()

# Create the course table
#create_db()

# Insert data into the course table
#insert_course('Maths I', '3 months', 'RM300', 'Basic Maths')
#insert_course('Physics I', '4 months', 'RM400', 'Basic Physics')
