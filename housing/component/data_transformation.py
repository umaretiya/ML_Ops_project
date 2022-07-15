from housing.exception import HousingException
from housing.logger import logging
from housing.entity.config_entity import DataTransformationConfig
from housing.entity.artifact_entity import (DataTransformationArtifact,
                                            DataIngestionArtifact,DataValidationArtifact)
from housing.constant import * 
from housing.util.util import read_yaml_file,save_object,save_numpy_array_data,load_data

import os,sys,numpy as np,pandas as pd

from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.base import BaseEstimator,TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer


class FeatureGenerator(BaseEstimator, TransformerMixin):
    
    def __init__(self, add_bedrooms_per_room=True,
                 total_rooms_ix=3,
                 population_ix=5,
                 households_ix=6,
                 total_bedrooms_ix=4, columns=None):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    def fit(self,X,y=None):
        return self 
    
    
    def transform(self, X,y=None):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
        
class DataTransformation:
    def __init__(self, data_transformation_config,data_ingestion_artifact,
                 data_validation_artifact):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e
    
    def get_data_transformer_object(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def initiate_data_transformation(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    def __del__(self):
        logging.info(f"{'>>'*30}Data Transformation log completed. {'<<'*30} \n\n")
        
        