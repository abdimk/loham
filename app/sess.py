import sqlite3

def clean_session_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('companies.db')
    cursor = conn.cursor()

    # Execute the DELETE statement to clean up the session table
    cursor.execute("DELETE FROM user_session")

    # Commit the transaction and close the connection
    conn.commit()
    conn.close()

# Call the function to clean up the session table
clean_session_table()
