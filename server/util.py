import json
import pickle
import os
import numpy as np

__locations=None
__data_columns=None
__model=None

def get_estimated_price(location, sqft, bhk, bath):
    # as __datacolumns is a python list, so we find its index using .index
    # as .index throws error when index is not found, so we wrap it up in try catch
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index=-1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index >= 0:
        x[loc_index] = 1
    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations

def load_saved_artifacts():
    print("loading saved artifacts start")
    global __locations
    global __data_columns

    # SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    # file_path=os.path.join(SITE_ROOT, "artifacts", "columns.json")
    file_path='./artifacts/columns.json'
    with open(file_path, "r") as f:
        __data_columns=json.load(f)['data_columns']
        __locations = __data_columns[3:]

    global __model
    file_path2='./artifacts/Bengaluru_House_Data.pickle'
    # with open(os.path.join(SITE_ROOT, "artifacts", "Bengaluru_House_Data.pickle"), 'rb') as f:
    with open(file_path2, 'rb') as f:
        __model = pickle.load(f)
    print("loading artifacts is done")

if __name__ == "__main__":
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('vittasandra', 1000, 2, 3))
    print(get_estimated_price('gwalior', 1000, 2, 3))