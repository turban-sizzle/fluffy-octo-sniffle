from flask import Flask
import json
import datetime
import os

app = Flask(__name__)

class Water():

    @staticmethod
    def read_water(water_path = './water.json'):
        water = {}
        if os.path.isfile(water_path):
            with open(water_path, 'r') as f:
                data = f.read()
                water = json.loads(data)
        return water

    def read_water_by_user(userId, water_prefix = 'water'):
        water = {}
        water_path = f'./{water_prefix}_{userId}.json'
        if os.path.isfile(water_path):    
            with open(water_path, 'r') as f:
                data = f.read()
                water = json.loads(data)
        return water

    def save_water(water, water_path='./water.json'):
        with open(water_path, 'w') as f:
            f.write(json.dumps(water))


    def save_water_by_user(water, userId, water_prefix='water'):
        with open(f'./{water_prefix}_{userId}.json', 'w') as f:
            f.write(json.dumps(water))

# Ajoute de l'eau
@app.route('/add_water', methods=['GET'])
def add_water():
    water = Water.read_water()
    if 'water' in water:
        print(water)
        water["water"] += 10
        if not "adding" in water.keys():
            water["adding"] = [{'added_at': str(datetime.datetime.now()), 'quantity': 10}]
            return Water.save_water(water)
        else:
            water["adding"].append({'added_at': datetime.datetime.now(), 'quantity': 10})
            return Water.save_water(water)
    return water

import tempfile

# Get water
@app.route('/water', methods=['GET'])
def water():
    filename = tempfile.mktemp()
    logfile = open(filename, 'a')
    logfile.write(f'getting water at {datetime.datetime.now()}')
    return Water.read_water()
    logfile.close()


@app.route('/add_water/<user_id>')
def add_water_user(user_id):
    water = Water.read_water_by_user(userId=user_id)
    if 'water' in water:
        print(water)
        water["water"] += 10
        Water.save_water_by_user(water, user_id)
    return water

@app.route('/add_alert/<user_id>')
def check_alert(user_id):
    water = Water.read_water_by_user(userId=user_id)
    if 'water' in water:
        if water['water'] < 10:
            return 'alert missing water'
        else:
            return 'everything is ok'
    return 'missing water information'

if not __name__ == '__main__':
    print('using as import')
else:
    app.run(debug=True)

