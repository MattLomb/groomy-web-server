# A very simple Flask Hello World app for you to get started with...
import database as db
from flask import Flask, json, request, jsonify
from flask_restful import Resource

app = Flask(__name__)


db.dbInit()
tableName = "Pets"
#db.dropTable(tableName)

@app.route('/')
def hello_world():
    return 'Hello from Groomy!'

#Add a pet inside the pet db
@app.route('/pet', methods=['PUT','POST'] )
def add_pet():
    args = request.get_json()
    user_id = args['user_id']
    name = args['name']
    race = args['race']
    weight = args['weight']
    size = args['size']
    age = args['age']
    hair_type = args['hair_type']
    params = (user_id, name, race, weight, size, age, hair_type, )
    db.addPet(params)
    return 'OK'

#Get list of pets
@app.route('/pet', methods=['GET'] )
def get_pet():
    user_id = request.args.get('user_id')
    if user_id != '':
        print('Executing query')
        res = db.getPets(user_id)
        return res
    else:
        return 'KO'

#Delete a specific pet
@app.route('/pet', methods=['DELETE'] )
def delete_pet():
    pet_id = request.args.get('id')
    if pet_id != '':
        db.deletePet(pet_id)
        return 'OK'
    else:
        return 'KO'

#Add a shop
@app.route('/shop', methods=['PUT','POST'])
def add_shop():
    return 'Shop added!'

#Get a shop
@app.route('/shop', methods=['GET'])
def get_shop():
    return 'Shop id!'

#Remove a shop
@app.route('/shop', methods=['DELETE'])
def delete_shop():
    return 'Shop removed!'

#Add appointment
@app.route('/appointments', methods=['PUT', 'POST'] )
def add_appointment():
    return 'Appointment added'

#Get appointments
@app.route('/appointments', methods=['GET'] )
def get_appointments():
    return 'Appointments list'

#Remove appointments
@app.route('/appointments', methods=['DELETE'] )
def delete_appointment():
    return 'Appointment deleted'