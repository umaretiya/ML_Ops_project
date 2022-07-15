from housing.entity.config_entity import DataIngestionConfig 
from housing.entity.artifact_entity import DataIngestionArtifact
from housing.exception import HousingException
from housing.logger import logging

import os,sys,tarfile
from six.moves import urllib

import pandas as pd 
import numpy as np
from sklearn.model_selection import StratifiedShuffleSplit


class DataIngestion:
    def __init__(self,data_ingestion_config) -> None:
        try:
            logging.info(f"{'>>'*20}Data Ingestion log started. {'<<'*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys)
        
        
    def download_housing_data(self,):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
    
    
    def extract_tgz_file(self, tgz_file_path):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def split_data_as_train_test(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e 
        
        
    def __del__(self):
        logging.info(f"{'>>'*20} Data Ingestion log completed.{'<<'*20} \n\n")