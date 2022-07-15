from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from housing.entity.config_entity import ModelTrainerConfig 
from housing.entity.model_factory import MetricInfoArtifact, ModelFactory, GridSearchedBestModel,evaluate_regression_model
from housing.util.util import load_numpy_array_data,save_object,load_object

import sys
from typing import List


class HousingEstimatorModel:
    def __init__(self, preprocessing_object, trained_model_object):
        self.preprocessing_object = preprocessing_object
        self.trained_model_object = trained_model_object

    def predict(self, X):
        transformed_feature = self.preprocessing_object.transform(X)
        return self.trained_model_object.predict(transformed_feature)
    
    def __repr__(self) -> str:
        return f"{type(self.trained_model_object).__name__}()"
    
    def __str__(self) -> str:
        return f"{type(self.trained_model_object).__name__}()"
    

class ModelTrainer:
    
    def __init__(self, model_trainer_config, data_transformation_artifact):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def initiate_model_trainer(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    def __del__(self):
        logging.info(f"{'>>' * 30}Model trainer log completed.{'<<' * 30} ")