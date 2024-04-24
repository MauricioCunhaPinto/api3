import mysql.connector

def connect_to_db():
    # Establish a connection to the database
    conn = mysql.connector.connect(
        user='root',
        password='',
        host='localhost',
        database='comodato'
    )
    return conn