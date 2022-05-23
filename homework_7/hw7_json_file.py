import json
from dataclasses import asdict
from hw7_data_class import DataCar


tesla = DataCar(name='Tesla', color='White', year=2018, speed_limit=250)

data_dict = asdict(tesla)

""" Create or update a JSON file """
with open('cars.json', 'w') as json_file:
    json.dump(data_dict, json_file, indent=4)

""" Read the JSON file """
with open('cars.json') as json_file:
    print(json.load(json_file))


