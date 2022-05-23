import json
from dataclasses import asdict
from hw7_data_class import DataCar


data = {'cars': []}
tesla = DataCar(name='Tesla', color='White', year=2018, speed_limit=250)
bmw = DataCar(name='BMW', color='Black', year=2006, speed_limit=200)


def equal_cars_year(obj_1: object, obj_2: object) -> bool:
    return obj_1 > obj_2


print(equal_cars_year(tesla, bmw))


cars_list = [tesla, bmw]


def dict_objects(list_with_cars: list):
    """ Object to dictionary """
    for i in list_with_cars:
        data_dict = asdict(i)
        data['cars'].append(data_dict)
    return data


""" Create or update a JSON file """
with open('cars.json', 'w') as json_file:
    json.dump(dict_objects(cars_list), json_file, indent=4)  # dump - serialization python object to JSON


""" Read the JSON file """
with open('cars.json') as json_file:
    print(json.load(json_file))  # load - deserialization JSON to python object



