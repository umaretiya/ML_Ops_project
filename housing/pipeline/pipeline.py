from housing.exception import HousingException
from housing.logger import logging
from housing.constant import * 
from housing.config.configuration import Configuration
from housing.entity.artifact_entity import (DataIngestionArtifact,DataTransformationArtifact,DataValidationArtifact,
                                            ModelPusherArtifact,ModelEvaluationArtifact,ModelTrainerArtifact)
from housing.entity.config_entity import DataIngestionConfig, ModelEvaluationConfig
from housing.component.data_ingestion import DataIngestion
from housing.component.data_validation import DataValidation
from housing.component.data_transformation import DataTransformation
from housing.component.model_trainer import ModelTrainer
from housing.component.model_evaluation import ModelEvaluation
from housing.component.model_pusher import ModelPusher

import uuid,os,sys,pandas as pd
from datetime import datetime
from collections import namedtuple
from threading import Thread
from typing import List


Experiment =namedtuple("Experiment", ["experiment_id","initialization_timestamp","artifact_time_stamp",
                                      "running_status","start_time","stop_time","execution_time","message",
                                      "experiment_file_path","accuracy","is_model_accepted"])


class Pipeline(Thread):
    experiment = Experiment(*([None] * 11))
    experiment_file_path = None 
    
    def __int__(self, config):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def start_data_ingestion(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def start_data_validation(self, data_ingestion_artifact):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def start_data_transformation(self,data_ingestion_artifact,
                                  data_validation_artifact):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def start_model_trainer(self, data_transformation_artifact):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    def start_model_evaluation(self, data_ingestion_artifact,
                               data_validation_artifact,
                               model_trainer_artifact):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def start_model_pusher(self, model_eval_artifact):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def run_pipeline(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
    def run(self):
        try:
            self.run_pipeline()
        except Exception as e:
            raise e 
        
        
    def save_experiment(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
    @classmethod
    def get_experiments_status(cls, limit):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
