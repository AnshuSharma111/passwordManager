import sqlite3
import bcrypt
import json
import os
import ctypes
import base64
from cryptography.fernet import Fernet

basedir = os.path.dirname(__file__)
databasePath = os.path.join(basedir, 'userdata.db')
credentialsFilePath = os.path.join(basedir, 'credentials.json')

curIndex = 0
conn, cursor = None, None
key = None

# Initialisation Function
def initialise() -> list:
    print("Starting Initialisation....")
    global conn, cursor, curIndex, key
    conn = sqlite3.connect(databasePath)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS userData(Id integer PRIMARY KEY,
        Title TEXT,
        Username TEXT,
        Password TEXT)''')

    # Get Key
    key = getKey()
    print(f"KEY : {key}\n")

    # Calculate latest Index
    renderData, curIndex = retrieveFromDatabase() 

    return renderData

# Function Called when application is exited
def closeConnection():
    print("Closing Application...")
    if not conn:
        return
    cursor.close()
    conn.close()

# Add record to Database
def addToDatabase(title, username, password):
    global curIndex

    # Encrypt the data
    cipher = Fernet(key)
    encrypted_title = cipher.encrypt(title.encode())
    encrypted_username = cipher.encrypt(username.encode())
    encrypted_password = cipher.encrypt(password.encode())

    encrypted_title_b64 = base64.b64encode(encrypted_title).decode('utf-8')
    encrypted_username_b64 = base64.b64encode(encrypted_username).decode('utf-8')
    encrypted_password_b64 = base64.b64encode(encrypted_password).decode('utf-8')
    print(f"Encrypted: {encrypted_title_b64} {encrypted_username_b64} {encrypted_password_b64}")

    curIndex += 1
    cursor.execute('''
        INSERT INTO userData VALUES(?, ?, ?, ?)
    ''', (curIndex, encrypted_title_b64, encrypted_username_b64, encrypted_password_b64))

    print("Inserted into table record: ", curIndex, title, username, password)

    conn.commit()

def retrieveFromDatabase():
    data = cursor.execute('SELECT * FROM userdata').fetchall()

    render_data = []
    cipher = Fernet(key)
    
    print("Retrieving Data...\n")
    for row in data:
        print(row)
        encrypted_title = base64.b64decode(row[1])
        encrypted_username = base64.b64decode(row[2])
        encrypted_password = base64.b64decode(row[3])

        decrypted_title = cipher.decrypt(encrypted_title).decode('utf-8')
        decrypted_username = cipher.decrypt(encrypted_username).decode('utf-8')
        decrypted_password = cipher.decrypt(encrypted_password).decode('utf-8')

        render_data.append((row[0], decrypted_title, decrypted_username, decrypted_password))
    return (render_data, len(render_data))

def fetchLatestData()-> any:
    data = cursor.execute('SELECT * FROM userdata ORDER BY id DESC LIMIT 1').fetchone()

    cipher = Fernet(key)
    encrypted_title = base64.b64decode(data[1])
    encrypted_username = base64.b64decode(data[2])
    encrypted_password = base64.b64decode(data[3])

    decrypted_title = cipher.decrypt(encrypted_title).decode('utf-8')
    decrypted_username = cipher.decrypt(encrypted_username).decode('utf-8')
    decrypted_password = cipher.decrypt(encrypted_password).decode('utf-8')

    return (data[0], decrypted_title, decrypted_username, decrypted_password)

def deleteFromDatabase(indices) -> None:
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

def restructure(index) -> None:
    cursor.execute("UPDATE userData SET id = id - 1 WHERE id > ?", (index,))
    conn.commit()

def checkMasterPassword() -> bool:
    try:
        with open(credentialsFilePath, 'r') as f:
            data = json.load(f)
            password = data['master password']
            print(password)

            if not password:
                return False
            else:
                return True
    except:
        print("Master Password does not exist!")
        return False

def setMasterPassword(password) -> None:
    # If there is no key, then the application must have been opened for the first time, therefore we generate key
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode(), salt)

    key = Fernet.generate_key()

    with open(credentialsFilePath, 'w') as f:
        json.dump({
            'master password':hashed_password.hex(),
            'key': key.hex()
        }, f)
    ctypes.windll.kernel32.SetFileAttributesW(credentialsFilePath, 2)
    print("Security key/ Key set up successfully!")

def getMasterPassword() -> bytes:
    with open(credentialsFilePath, 'r') as f:
        data = json.load(f)
    mPass = bytes.fromhex(data['master password'])
    return mPass

def getKey() -> tuple:
    with open(credentialsFilePath, 'r') as f:
        key_iv_data = json.load(f)
    key = bytes.fromhex(key_iv_data['key'])
    return key

def authenticate(text) -> bool:
    print("Entered Password: ", text)
    masterPassword = getMasterPassword()

    return bcrypt.checkpw(text.encode(), masterPassword)