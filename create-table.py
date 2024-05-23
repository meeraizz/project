import sqlite3

def drop_course_table():
    # Connect to the database
    con = sqlite3.connect(database="GradeMaster.db")
    cur = con.cursor()
    
    # Drop the course table if it exists
    cur.execute("DROP TABLE IF EXISTS course")
    
    # Commit the changes and close the connection
    con.commit()
    con.close()

# Call the drop_course_table function to delete the table
drop_course_table()

def drop_result_table():
    # Connect to the database
    con = sqlite3.connect(database="GradeMaster.db")
    cur = con.cursor()
    
    # Drop the course table if it exists
    cur.execute("DROP TABLE IF EXISTS result")
    
    # Commit the changes and close the connection
    con.commit()
    con.close()

# Call the drop_course_table function to delete the table
drop_result_table()
