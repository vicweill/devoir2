from psycopg2 import connect
from psycopg2.errors import DuplicateTable, DatabaseError
import os

def connect_to_db_server():
    """ Connect to database server with provided environment variables """
    try:
        connection = connect(
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                database=os.getenv("POSTGRES_DB"),
                host="db",
                port="5432")
        cursor = connection.cursor()
        print("Successfully connected to Postgres Server\n")
        return connection
    except Exception as e:
        print(f"could not connect to the postgres {e}\n")

def create_new_table(connection):
    """ Create a new table in the default db"""

    query = """ CREATE TABLE persons ( 
                    id SERIAL, 
                    first_name VARCHAR(50),
                    last_name VARCHAR(50),
                    date_of_birth VARCHAR(20),
                    email VARCHAR(100),
                    PRIMARY KEY (id)
                    ) """
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Created table successfully\n")
    except DuplicateTable as e:
        print("The table already exist, skipping.\n")
        connection.rollback()
    except (Exception, DatabaseError) as error:
        print(error)
        connection.rollback()
        if connection is not None:
            connection.close()
        


def insert_rows_to_table(connection, table, rows):
    """ rows should be of the form of a list of tuples"""
    query = """ INSERT INTO persons(id, first_name, last_name, date_of_birth, email) VALUES (%s)"""
    cursor = connection.cursor()
    # insert multiple rows at once
    cursor.executemany(query, rows)
    # commit
    connection.commit()
    print(f"Added rows successfully:\n{row}\n")

def csv_to_table(connection, table, data_path):
    try:
        cursor = connection.cursor()
        with open(data_path) as f:
            cursor.copy_from(f, table, sep=",", columns=('first_name', 'last_name', 'date_of_birth', 'email'))
        connection.commit()
        print("Added the CSV successfully !")
    except (Exception, DatabaseError) as error:
        print(error)
        connection.rollback()
        if connection is not None:
            connection.close()

# what's the difference between a server side cursor and client side cursor (apprently you can't use a server side cursor to create a table): https://stackoverflow.com/questions/51804513/psycopg2-syntax-error-at-or-near-update