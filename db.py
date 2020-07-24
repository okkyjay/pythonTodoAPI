# db_utils.py
import os
import sqlite3

# create a default path to connect to and create (if necessary) a database
# called 'database.sqlite3' in the same directory as this script
DEFAULT_PATH = './todo.db'

def db_connect(db_path=DEFAULT_PATH):
    con = sqlite3.connect(db_path)
    return con
