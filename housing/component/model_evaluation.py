from tkinter import E
from housing.logger import logging
from housing.exception import HousingException
from housing.constant import *
from housing.entity.config_entity import ModelEvaluationConfig
from housing.entity.artifact_entity import (DataIngestionArtifact,DataValidationArtifact,ModelTrainerArtifact,ModelEvaluationArtifact)
from housing.util.util import write_yaml_file,read_yaml_file,load_object,load_data
from housing.entity.model_factory import evaluate_regression_model

import numpy as np,os,sys 



class ModelEvaluation:
    
    def __init__(self, model_evaluation_config,
                 model_trainer_artifact,
                 data_ingestion_artifact,
                 data_validation_artifact):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 

    
    def get_best_model(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
    def update_evaluation_report(self, model_evaluation_artifact):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
    def initiate_model_evaluation(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def __del__(self):
        logging.info(f"{'=' * 20}Model Evaluation log completed.{'=' * 20} ")
