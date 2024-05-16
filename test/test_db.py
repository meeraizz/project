import sqlite3




#Querry the DB and RETURN ALL records
def show_all():

    # Connect to the database
    conn = sqlite3.connect('customer.db')

    # Create cursor
    c = conn.cursor()
    #drop table
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # Commit the transaction
    conn.commit()

    # Close the connection
    conn.close()