import pickle
import json
import numpy as np

__locations = None
__data_columns = None
__model = None

def get_estimated_price(location,sqft,bhk,bath):
    try:
        loc_index = __data_columns.index(location.lower())
    except:
        loc_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bath
    x[2] = bhk
    if loc_index>=0:
        x[loc_index] = 1

    return round(__model.predict([x])[0],2)


# Pulling 'Models.pickle' and 'columns.json' file from artifacts 
def load_saved_artifacts():
    print("loading saved artifacts...start")
    #setting the locations,data columns, and model as global variable
    global  __data_columns
    global __locations
#1) Calling Columns.json file and storing its values into the global variables
    with open("artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']#Loading all columns from file and storing in __data_columns
        __locations = __data_columns[3:]  # Loading all locations in variable

    global __model
#2) Loading Pickle file in 'model' variable
    if __model is None:
        with open('artifacts/bangalore_home_price_prediction.pickle', 'rb') as f:
            __model = pickle.load(f)
    print("loading saved artifacts...done")

def get_location_names():
    return __locations

def get_data_columns():
    return __data_columns

if __name__ == '__main__':
    load_saved_artifacts()
    print(get_location_names())
    print(get_estimated_price('1st Phase JP Nagar',1000, 3, 3))
    print(get_estimated_price('1st Phase JP Nagar', 1000, 2, 2))
    print(get_estimated_price('Kalhalli', 1000, 2, 2)) # other location
    print(get_estimated_price('Ejipura', 1000, 2, 2))  # other location