import json
from homework_7.hw7_data_class import DataCar


with open('model_car.json') as json_file:
    file = json.load(json_file)

comment = DataCar(file)

