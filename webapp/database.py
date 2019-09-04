import sqlite3
from sqlite3 import Error
 
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(conn, user):
    """
    Create a new user
    :param conn:
    :param user:
    :return:
    """
 
    sql = ''' INSERT INTO users(username,password)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, user)
    return cur.lastrowid
 
def execute_query(conn, query):
    """
    Executes a query agains the database
    :param conn:
    :param query:
    :return:
    """

    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def create_users_table(conn):
        
    sql_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                        id integer PRIMARY KEY,
                                        username text NOT NULL,
                                        password text
                                    ); """
    with conn:
        # create users table
        create_table(conn, sql_users_table)

def populate_users(conn):
    # create tables
    with conn:
        users = [
            ('mar', 'bean'),
            ('jee', 'willow'),
            ('mug', 'box'),
            ('trout', 'tuna'),
            ('sport', 'dog'),
            ('root', 'mug')
        ]
        for user in users:
            create_user(conn, user)

def remove_all_users(conn):
    # remove existing entries in users table
    execute_query(conn, "DELETE FROM users;")

def get_database_handle(database_name):
    return create_connection(database_name)

def initalize_database():
    database = r"users.db"

    # create a database connection
    conn = create_connection(database)

    # remove existing users
    try:
        remove_all_users(conn)
    except:
        pass

    # create users table if it doesn't exist
    create_users_table(conn)

    # populate users
    populate_users(conn)


if __name__ == '__main__':
    main()