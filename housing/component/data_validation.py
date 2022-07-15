from tkinter import E
from housing.logger import logging
from housing.exception import HousingException

from housing.entity.config_entity import DataValidationConfig
from housing.entity.artifact_entity import DataValidationArtifact

import os,sys,json,pandas as pd

class DataValidation:
    
    def __init__(self, data_validation_config,
                 data_ingestion_artifact):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
    def get_train_and_test_df(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    def is_train_test_file_exists(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e,sys) from e 
        
    def validate_dataset_schema(self):
        try:
            validation_status = False
            # validation of data set
            validation_status = True
            return validation_status
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def get_and_save_data_drift_report(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    def save_data_drift_report_page(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
    
    def is_data_drift_found(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def initiate_data_validation(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    def __del__(self):
        logging.info(f"{'>>'*30}Data Validation log completed. {'<<'*30} \n\n")
        