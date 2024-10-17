import sqlite3
import os

basedir = os.path.dirname(__file__)
databasePath = os.path.join(basedir, 'userdata.db')

conn = None
cursor = None

def initialise():
    print("Starting Initialisation")
    global conn
    global cursor
    conn = sqlite3.connect(databasePath)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS userData(Id integer PRIMARY KEY AUTOINCREMENT,
        Title varchar(20),
        Username varchar(50),
        Password varchar(50))''')

def closeConnection():
    if not conn:
        return
    cursor.close()
    conn.close()

def authenticate(text):
    print(text)
    return True

def addToDatabase(title, username, password):
    if not cursor:
        initialise()

    cursor.execute('''
        INSERT INTO userData (Title, Username, Password) VALUES(?, ?, ?)
    ''', (title, username, password))

    conn.commit()

def fetchLatestData():
    if not cursor:
        initialise()
    
    data = cursor.execute('''SELECT * FROM userData
        ORDER BY id DESC
        LIMIT 1''')
    
    return data.fetchone()