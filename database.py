from os import renames
import sqlite3, random
from datetime import date
from sqlite3.dbapi2 import Date
from model import Database
import json

DATABASE = './groomy.db'

database = Database()

def getDb():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE)
    except sqlite3.error as e:
        print(e)
    return conn

def queryDb(query, args=(), one=False):
    conn = getDb()
    cur = conn.execute(query, args)
    conn.commit()
    rv = cur.fetchall()
    cur.close()
    #print(rv)
    return (rv[0] if rv else None) if one else rv

# Startup the db: create Pets, Shops and Appointments tables
def dbInit():
    query = """CREATE TABLE IF NOT EXISTS Pets ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    name TEXT,
                    race TEXT,
                    weight REAL,
                    size TEXT,
                    age NUMERIC,
                    hair_type TEXT
                )"""
    queryDb(query)
    print("Pets table OK")
    query = """CREATE TABLE IF NOT EXISTS Shops ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT,
                    shop_name TEXT,
                    address TEXT,
                    hours TEXT,
                    telephone NUMERIC,
                    email TEXT
                )"""
    queryDb(query)
    print("Shops table OK")
    print("DB STARTED WITH SUCCESS!")

# Retrieve pets for a specific user
def getPets( user_id ):
    query = """SELECT * FROM Pets WHERE user_id=?"""
    args = (user_id,)
    res = queryDb( query, args )
    return json.dumps(res)
    
# Add a new pet
def addPet( args ):
    query = """INSERT INTO Pets (user_id, name, race, weight, size, age, hair_type ) VALUES (?,?,?,?,?,?,?)"""
    queryDb(query,args)
    print("Pet added with success!")
    
# Delete a specific pet
def deletePet( args ):
    query = """DELETE FROM Pets WHERE id = """ + args
    queryDb(query)
    print("Pet with ID= " + args + " deleted with success")
    return 'OK'

# Add a new shop
def addShop( args ):
    query = """INSERT INTO Shops (user_id, shop_name, address, hours, telephone, email ) VALUES (?, ?, ?, ?, ?, ?)"""
    queryDb(query, args)
    print("Shop added with success!")
    
# Retrieve the shop for a particular user
def getShop( user_id ):
    query = """SELECT * FROM Shops WHERE user_id=?"""
    args = (user_id,)
    res = queryDb( query, args )
    return json.dumps(res)

# Remove a shop from db
def deleteShop( args ):
    query = """DELETE FROM Shops WHERE id = """ + args
    queryDb(query)
    print("Shop with ID= " + args + " deleted with success")
    return 'OK'

# UTILS
def printQuery():
    print("test")
    
def dropTable(tableName):
    query = 'DROP TABLE IF EXISTS ' + tableName 
    queryDb(query)
    print("table removed with success")