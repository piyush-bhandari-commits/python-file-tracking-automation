import os
import sys
import sqlite3
from sqlite3 import Error

"""Returns the name of the SQLite DB file"""
def getbasefile():
    return os.path.splitext(os.path.basename(__file__))[0]

"""Connects to the SQLite DB"""
def connectdb():
    try:
        dbfile = getbasefile() + '.db'
        conn = sqlite3.connect(dbfile , timeout=2)
        print (sqlite3.version)

    except Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
            print("The conncection is closed to the database")
