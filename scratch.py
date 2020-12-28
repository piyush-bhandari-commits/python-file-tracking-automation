import os
import sys
import sqlite3
from sqlite3 import Error

def get_basefile():
    """
    Returns the name of the SQLite DB file
    """
    return os.path.splitext(os.path.basename(__file__))[0]

def create_connection():
    """
    Connects to the SQLite DB
    """
    conn = None

    try:
        dbfile = get_basefile() + '.db'
        conn = sqlite3.connect(dbfile , timeout=2)
        cur = conn.cursor()

    except Error as e:
        print(e)

    return conn, cur

class FileChangeDatabase:

    def __init__(self,):
        """
        Initiates the cursor and connection object to the database
        """
        self.conn, self.cur = create_connection()
        print("\nConnection to database OPENED successfully...\n")
    
    def create_table(self, table_name):
        """
        Method used to create different tables in the database
        """
        self.cur.execute("CREATE TABLE {} IF NOT EXISTS".format(table_name))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        print("Table with name: {} created successfully...".format(table_name))

    def create_table_index(self, table_name, index_name):
        """
        Method used to create index for different tables in the database
        """
        self.cur.execute("CREATE INDEX {} ON {}".format(table_name, index_name))
        rows = self.cur.fetchall()
        for row in rows:
            print(row)
        print("Index with name {} on table {} created successfully...".format(index_name, table_name))
        pass

    def close_connection(self,):
        if self.conn != None:
            self.conn.close()
            print("\nConnection to database CLOSED successfully...\n")

    
if __name__ == "__main__":

    db_instance = FileChangeDatabase()

    db_instance.close_connection()