import yaml
import dill
import numpy as np
import pandas as pd 
from housing.constant import *
import os, sys 
from housing.exception import HousingException

def write_yaml_file(file_path,data):
    try:
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "w") as yaml_file:
            yaml.dump(data, yaml_file)
            
    except Exception as e:
        raise HousingException(e,sys) from e


def read_yaml_file(file_path):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e 


def save_numpy_array_data(file_path, array):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            np.save(file_obj, array)
            
    except Exception as e:
        raise HousingException(e, sys) from e

    
def load_numpy_array_data(file_path):
    try:
        with open(file_path, "rb") as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e
    
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path,"wb") as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e
    
def load_object(file_path):
    try:
        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)
    except Exception as e:
        raise HousingException(e, sys) from e
    
def load_data(file_path, schema_file_path):
    try:
        dataset_schema = read_yaml_file(schema_file_path)
        schema = dataset_schema[DATASET_SCHEMA_COLUMNS_KEY]
        
        dataframe = pd.read_csv(file_path)
        error_message = ""
        
        for column in dataframe.columns:
            if column in list(schema.keys()):
                dataframe[column].astype(schema[column])
            else:
                error_message = f"{error_message} \nColumn: [{column}] is not in the schema."
        if len(error_message) > 0:
            raise Exception(error_message)
        return dataframe
    
    except Exception as e:
        raise HousingException(e, sys) from e