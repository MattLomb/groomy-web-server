# A very simple Flask Hello World app for you to get started with...
import database as db
from flask import Flask, json, request, jsonify
from flask_restful import Resource

app = Flask(__name__)


db.dbInit()
#tableName = "Appointments"
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
        return jsonify(res)
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
    args = request.get_json()
    user_id = args['user_id']
    shop_name = args['shop_name']
    address = args['address']
    hours = args['hours']
    telephone = args['telephone']
    email = args['email']
    params = (user_id, shop_name, address, hours, telephone, email, )
    db.addShop(params)
    return 'Shop added!'

#Get a shop
@app.route('/shop', methods=['GET'])
def get_shop():
    user_id = request.args.get('user_id')
    if user_id == 'ALL':
        print("retrieving all shops in the application")
        res = db.getAllShop()
        return jsonify(res)
    if user_id != '':
        print('Executing query')
        res = db.getShop(user_id)
        return jsonify(res)
    else:
        return 'KO'

#Remove a shop
@app.route('/shop', methods=['DELETE'])
def delete_shop():
    shop_id = request.args.get('id')
    if shop_id != '':
        db.deleteShop(shop_id)
        return 'OK'
    else:
        return 'KO'

#Add appointment
@app.route('/appointments', methods=['POST'] )
def add_appointment():
    args = request.get_json()
    pet_owner = args['pet_owner']
    shop_owner = args['shop_owner']
    shop_name = args['shop_name']
    pet = args['pet']
    date = args['date']
    hour = args['hour']
    status = args['status']
    lavaggio = args['lavaggio']
    taglio_pelo = args['taglio_pelo']
    taglio_unghie = args['taglio_unghie']
    spa = args['spa']
    anti_parassitario = args['anti_parassitario']
    params = (pet_owner, 
              shop_owner,
              shop_name,
              pet,
              date,
              hour,
              status,
              lavaggio,
              taglio_pelo,
              taglio_unghie,
              spa,
              anti_parassitario,
            )
    db.addAppointment( params )
    return 'OK'

#Get appointments
@app.route('/appointments', methods=['GET'] )
def get_appointments():
    user_id = request.args.get('user_id')
    res = db.getAppointments(user_id)
    return jsonify(res)

#Remove appointments
@app.route('/appointments', methods=['DELETE'] )
def delete_appointment():
    id = request.args.get('id')
    db.deleteAppointment(id)
    return 'OK'

#Update the status of a given appointment
@app.route('/appointments', methods=['PUT'] )
def update_appointment():
    args = request.get_json()
    id = args['id']
    status = args['status']
    db.updateAppointment(id, status)
    return 'OK'