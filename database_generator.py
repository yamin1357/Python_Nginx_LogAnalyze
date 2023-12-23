import sqlite3
from sqlite3 import Error
from global_statics import DATABASE_NAME
from sql_scripts import CREATE_LOGS_TBL


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print("create_connection", e)

    return conn


def create_table(conn, create_table_sql):
    print(create_table_sql)
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print("create_table", e)


def start_database_generation():
    confirm = input("Sure wanna create database and table ? yes : 1, no: 2 ===> ")
    if confirm == '1':
        db_file = DATABASE_NAME
        sqlite_connection = None

        try:
            print("Establishing connection is started ...")
            sqlite_connection = create_connection(db_file)
            print("Connection to sqlite has been established successfully.")
            create_table(sqlite_connection, CREATE_LOGS_TBL)
        except Error as e:
            print("Error occured while connecting to sqlite3 database.")

        finally:
            if sqlite_connection:
                sqlite_connection.close()
                print("sqlite connection closed.")


if __name__ == '__main__':
    start_database_generation()
