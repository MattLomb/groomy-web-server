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
    print(rv)
    return (rv[0] if rv else None) if one else rv

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
    print("DB STARTED WITH SUCCESS!")
   
def getPets( user_id ):
    query = """SELECT * FROM Pets WHERE user_id=?"""
    args = (user_id,)
    res = queryDb( query, args )
    return json.dumps(res)
    
def addPet( args ):
    query = """INSERT INTO Pets (user_id, name, race, weight, size, age, hair_type ) VALUES (?,?,?,?,?,?,?)"""
    queryDb(query,args)
    print("Pet added with success!")
    
def deletePet( args ):
    query = """DELETE FROM Pets WHERE id = """ + args
    queryDb(query)
    print("Pet with ID= " + args + " deleted with success")
    return 'OK'
    
def printQuery():
    print("test")
    
def dropTable(tableName):
    query = 'DROP TABLE IF EXISTS ' + tableName 
    queryDb(query)
    print("table removed with success")