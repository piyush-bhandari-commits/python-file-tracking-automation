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
        self.conn, self.cur = create_connection()
        print("\nConnection to database OPENED successfully...\n")

    def create_table(self, query):
        """
        This method is used to create different tables in the database
        """

        pass

    
    
    
    def close_connection(self,):
        if self.conn != None:
            self.conn.close()
            print("Connection to database CLOSED successfully...")

if __name__ == "__main__":
    
    pass