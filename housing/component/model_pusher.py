from housing.exception import HousingException
from housing.logger import logging
from housing.entity.artifact_entity import ModelPusherArtifact, ModelEvaluationArtifact
from housing.entity.config_entity import ModelPusherConfig

import os,sys,shutil

class ModelPusher:
    
    def __init__(self, model_pusher_config,model_evaluation_artifact):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
    
    def export_model(self):
        try:
            pass
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def initiate_model_pusher(self):
        try:
            pass 
        except Exception as e:
            raise HousingException(e, sys) from e 
        
        
    def __del__(self):
        logging.info(f"{'>>' * 20}Model Pusher log completed.{'<<' * 20} ")