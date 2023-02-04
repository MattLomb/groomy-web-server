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
    query = """CREATE TABLE IF NOT EXISTS Appointments ( id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pet_owner TEXT,
                    shop_owner TEXT,
                    shop_name TEXT,
	                pet TEXT,
                    date DATETIME,
                    hour TEXT,
                    status NUMERIC,
                    lavaggio BOOLEAN,
	                taglio_pelo BOOLEAN,
	                taglio_unghie BOOLEAN,
	                spa BOOLEAN,
	                anti_parassitario BOOLEAN
                )"""
    queryDb(query)
    print("Appointments table OK")
    print("DB STARTED WITH SUCCESS!")

# Retrieve pets for a specific user
def getPets( user_id ):
    query = """SELECT * FROM Pets WHERE user_id=?"""
    args = (user_id,)
    res = queryDb( query, args )
    print(res)
    result = []
    for row in res:
        pet = {"id":row[0],
               "user_id":row[1],
               "name":row[2],
               "race":row[3],
               "weight":row[4],
               "size":row[5],
               "age":row[6],
               "hair_type":row[7]
            }
        result.append(pet)
    return result
    
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
    print(res)
    result = []
    for row in res:
        shop = {"id":row[0],
               "user_id":row[1],
               "shop_name":row[2],
               "address":row[3],
               "hours":row[4],
               "telephone":row[5],
               "email":row[6]
            }
        result.append(shop)
    return result

# Retrieve all shops in the application
def getAllShop():
    query = """SELECT * FROM Shops"""
    res = queryDb(query)
    result = []
    for row in res:
        shop = {"id":row[0],
               "user_id":row[1],
               "shop_name":row[2],
               "address":row[3],
               "hours":row[4],
               "telephone":row[5],
               "email":row[6]
            }
        result.append(shop)
    return result

# Remove a shop from db
def deleteShop( args ):
    query = """DELETE FROM Shops WHERE id = """ + args
    queryDb(query)
    print("Shop with ID= " + args + " deleted with success")
    return 'OK'

#Create a new appointment
def addAppointment( args ):
    query = """INSERT INTO Appointments (pet_owner, shop_owner, shop_name, pet, date, hour, status, lavaggio, taglio_pelo, taglio_unghie, spa, anti_parassitario ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    queryDb(query, args)
    print("APPOINTMENT CREATED")
    
# Retrieve appointment for a specific user
def getAppointments( user_id ):
    query = """SELECT * FROM Appointments WHERE pet_owner=? OR shop_owner=? ORDER BY date DESC"""
    args = (user_id, user_id)
    res = queryDb(query, args)
    result = []
    for row in res:
        shop = {"id":row[0],
               "pet_owner":row[1],
               "shop_owner":row[2],
               "shop_name" :row[3],
               "pet":row[4],
               "date":row[5],
               "hour":row[6],
               "status":row[7],
               "lavaggio":row[8],
               "taglio_pelo":row[9],
               "taglio_unghie":row[10],
               "spa":row[11],
               "anti_parassitario":row[12]
            }
        result.append(shop)
    return result
    
# Delete an appointment
def deleteAppointment( args ):
    query = """DELETE FROM Appointments WHERE id = """ + args
    queryDb(query)
    print("Appointment with ID= " + args + " deleted with success")
    return 'OK'

#Update appointment
def updateAppointment(id, status):
    query = """UPDATE Appointments SET status=? WHERE id=?"""
    args = (status, id,)
    queryDb(query,args)
    return 'STATUS UPDATED'
    
    
# UTILS
def printQuery():
    print("test")
    
def dropTable(tableName):
    query = 'DROP TABLE IF EXISTS ' + tableName 
    queryDb(query)
    print("table removed with success")