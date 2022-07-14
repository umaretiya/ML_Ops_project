import imp
import yaml
import os, sys 

from housing.exception import HousingException

def read_yaml_file(file_path):
    try:
        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e 