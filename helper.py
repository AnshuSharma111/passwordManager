import sqlite3
import os

basedir = os.path.dirname(__file__)
databasePath = os.path.join(basedir, 'userdata.db')

conn = None
cursor = None
curIndex = 0

def initialise():
    print("Starting Initialisation....")
    global conn
    global cursor
    global curIndex
    conn = sqlite3.connect(databasePath)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS userData(Id integer PRIMARY KEY,
        Title varchar(20),
        Username varchar(50),
        Password varchar(50))''')
    
    # Fetch all data and send it to UI to render
    data = cursor.execute('Select * from userData')

    # Calculate latest Index
    renderData = []
    for _ in data: 
        curIndex += 1
        renderData.append(_)
    print(f'{curIndex} entries in table')
    return renderData

def closeConnection():
    print("Closing Application...")
    if not conn:
        return
    cursor.close()
    conn.close()

def authenticate(text):
    print(text)
    return True

def addToDatabase(title, username, password):
    global curIndex

    curIndex += 1
    cursor.execute('''
        INSERT INTO userData VALUES(?, ?, ?, ?)
    ''', (curIndex, title, username, password))

    print("Inserted into table record: ",curIndex, title, username, password)

    conn.commit()

def deleteFromDatabase(indices):
    global curIndex

    deleted, num_deleted, prev_ind = "", 0, indices[0]
    for i in indices:
        if prev_ind < i:
            num_deleted += 1
        cursor.execute("DELETE FROM userData WHERE Id = ?", (i - num_deleted,))
        deleted = deleted + " " + str(i - num_deleted)
        restructure(i - num_deleted)
        prev_ind = i
    print(f"Deleted Indices: {deleted}")
    curIndex -= len(indices)

    conn.commit()

def restructure(index):
    cursor.execute("UPDATE userData SET id = id - 1 WHERE id > ?", (index,))
    conn.commit()
def fetchLatestData():
    data = cursor.execute('''SELECT * FROM userData
        ORDER BY id DESC
        LIMIT 1''')
    
    return data.fetchone()