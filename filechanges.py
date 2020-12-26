import os
import sys
import sqlite3
from sqlite3 import Error


def getbasefile():
    """
    Returns the name of the SQLite DB file
    """
    return os.path.splitext(os.path.basename(__file__))[0]

def connectdb():
    """
    Connects to the SQLite DB
    """
    try:
        dbfile = getbasefile() + '.db'
        conn = sqlite3.connect(dbfile , timeout=2)
        print ("Opened connection to database sucessfully")

    except Error as e:
        print(e)

    # finally:
    #     if conn:
    #         conn.close()
    #         print("The connection is closed to the database")

    return conn

def corecursor(conn, query, args):
    """
    Opens the sqlite database cursor
    """
    result = False
    cur = conn.cursor()
    
    try:
        cur.execute(query, args)
        rows = cur.fetchall()
        numrows = len(list(rows))
        if numrows > 0:
            result = True

    except Error as e:
        print(e)

    finally:
        if cur != None:
            cur.close()
    
    return result

def tableexists(table):
    """
    Checks if a SQLite DB Table exists
    """
    result = False

    try:
        conn = connectdb()
        if conn != None:
                   query = "SELECT name FROM sqlite_master WHERE type ='table' AND name NOT LIKE 'sqlite_%'" # Finish this query ...
                   args = (table,)
                   result = corecursor(conn, query, args)

    except Error as e:
        print(e)

    finally:
        if conn != None:
            conn.close()
            print("Closed connection to the database successfully")    
    return result

def createhashtable():
    """
    Creates a SQLite DB Table
    """
    result = False
    query = "CREATE TABLE files IF NOT EXISTS" # Finish this query ...
    try:
        conn = connectdb()
        if conn != None:
            if not tableexists('files'):
                try:
                    cursor = conn.cursor()
                    cursor.execute(query)
                except Error as e:
                    print(e)    
    finally:
        if conn != None:
            conn.close()
            print ("Connection to database closed successfully...")

    
if __name__ == "__main__":
    createhashtable()
