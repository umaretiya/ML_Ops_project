from housing.exception import HousingException
from housing.logger import logging
import importlib,yaml,os,sys, numpy as np

from cmath import log
from collections import namedtuple
from pyexpat import model
from typing import List

from sklearn.metrics import r2_score,mean_squared_error

GRID_SEARCH_KEY = 'grid_search'
MODULE_KEY = 'module'
CLASS_KEY = 'class'
PARAM_KEY = 'params'
MODEL_SELECTION_KEY = 'model_selection'
SEARCH_PARAM_GRID_KEY = 'search_param_grid'

InitializedModelDetail = namedtuple("InitializedModelDetail",
                                    ["model_serial_number","model","param_grid_search","model_name"])
GridSearchedBestModel =namedtuple("GridSearchedBestModel",["model_serial_number",
                                                           "model",
                                                           "best_model",
                                                           "best_parameters",
                                                           "best_score"])
BestModel = namedtuple("BestModel",["model_serial_number",
                                    "model",
                                    "best_model",
                                    "best_parameters",
                                    "best_score"])

MetricInfoArtifact = namedtuple("MetricInfoArtifact", ["model_name","model_object","train_rmse","test_rmse",
                                                      "train_accuracy","test_accuracy","model_accuracy","index_number"])

def evaluate_classification_model(model_list,X_train,y_train,X_test,y_test,base_accuracy:float=0.6):
    pass

def evaluate_regression_model(model_list,X_train,y_train,X_test,y_test,base_accuracy:float=0.6):
    try:
        index_number = 0
        metric_info_artifact = None
        for model in model_list:
            model_name = str(model)
            logging.info(f"{'>>'*30}Started evaluating model: [{type(model).__name__}] {'<<'*30}")
            
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            
            train_acc = r2_score(y_train,y_train_pred)
            test_acc = r2_score(y_test,y_test_pred)
            
            train_rmse = np.sqrt(mean_squared_error(y_train,y_train_pred))
            test_rmse = np.sqrt(mean_squared_error(y_test,y_test_pred))
            
            model_accuracy = (2* (train_acc*test_acc)) / (train_acc + test_acc)
            diff_test_train_acc = abs(test_acc - train_acc)
            
            logging.info(f"{'>>'*30} Score {'<<'*30} ")
            logging.info(f"Train Score\t\t Test Score\t\t Average Score")
            logging.info(f"{train_acc}\t\t {test_acc}\t\t {model_accuracy}")
            
            logging.info(f"{'>>'*30} Score {'<<'*30} ")
            logging.info(f"Diff test train acccuracy:[{diff_test_train_acc}]")
            logging.info(f"Train root mean squared error: [{train_rmse}]")
            logging.info(f"Test root mean Squared error:[{test_rmse}] ")
            
            if model_accuracy >= base_accuracy and diff_test_train_acc < 0.05:
                base_accuracy = model_accuracy
                metric_info_artifact = MetricInfoArtifact(model_name=model_name,
                                                          model_object=model,
                                                          train_rmse=train_rmse,
                                                          test_rmse=test_rmse,
                                                          train_accuracy=train_acc,
                                                          test_accuracy=test_acc,
                                                          model_accuracy=model_accuracy,
                                                          index_number=index_number,)
                
                logging.info(f"Acceptable model found {metric_info_artifact}.")
            index_number += 1
        if metric_info_artifact is None:
            logging.info(f"No model found with higher accuracy then base accuracy")
        return metric_info_artifact
                
    except Exception as e:
        raise HousingException(e,sys) from e


def get_sample_model_config_yaml_file(export_dir):
    try:
        model_config = {
            GRID_SEARCH_KEY: {
                MODULE_KEY: "sklearn.model_selection",
                CLASS_KEY: "GridSearchCV",
                PARAM_KEY: {
                    "cv": 3,
                    "verbose": 1
                }
            },
            MODEL_SELECTION_KEY:{
                "module_0": {
                    MODULE_KEY: "module_of_model",
                    CLASS_KEY: "ModelClassName",
                    PARAM_KEY:
                        {
                            "param_name1":"value1",
                            "param_name2":"value2",
                        },
                    SEARCH_PARAM_GRID_KEY: {
                        "param_name":["param_value_1","param_value_2"]
                            }
                    },
                }
        }
        os.makedirs(export_dir,exist_ok=True)
        export_file_path = os.path.join(export_dir,"model.yaml")
        with open(export_file_path, "w") as file:
            yaml.dump(model_config, file)
        return export_file_path
        
    except Exception as e:
        raise HousingException(e, sys) from e
    

class ModelFactory:
    def __init__(self, model_config_path):
        try:
            self.config = ModelFactory.read_params(model_config_path)
            self.grid_search_cv_modul = self.config[GRID_SEARCH_KEY][MODULE_KEY]
            self.grid_search_class_name= self.config[GRID_SEARCH_KEY][CLASS_KEY]
            self.grid_search_property_data =dict(self.config[GRID_SEARCH_KEY][PARAM_KEY])
            
            self.model_initialization_config = dict(self.config[MODEL_SELECTION_KEY])
            
            self.initialized_model_list = None
            self.grid_searched_best_model_list = None
            
        except Exception as e:
            raise HousingException(e, sys) from e
    
    
    @staticmethod
    def update_property_of_class(instance_ref, property_data):
        try:
            if not isinstance(property_data, dict):
                raise Exception("property_data parameter required to dictionary")
            for key,value in property_data.items():
                logging.info(f"Executing:$ {str(instance_ref)}.{key}={value}")
                setattr(instance_ref, key,value)
            return instance_ref
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    @staticmethod
    def read_params(config_path):
        try:
            with open(config_path) as yaml_file:
                config = yaml.safe_load(yaml_file)
            return config
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    @staticmethod
    def class_for_name(module_name, class_name):
        try:
            module = importlib.import_module(module_name)
            logging.info(f"Executin command: from{module} import {class_name}")
            class_ref = getattr(module, class_name)
            return class_ref
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    def execute_grid_search_operation(self, initialized_model,input_feature,
                                      output_feature):
        try:
            grid_search_cv_ref = ModelFactory.class_for_name(module_name=self.grid_search_cv_modul,
                                                             class_name=self.grid_search_class_name)
            grid_search_cv = grid_search_cv_ref(estimator=initialized_model.model,
                                                param_grid=initialized_model.param_grid_search)
            grid_search_cv = ModelFactory.update_property_of_class(grid_search_cv,
                                                                   self.grid_search_property_data)
            
            message = f'{">>"*30} f"Training {type(initialized_model.model).__name__} Started." {"<<"*30}'
            logging.info(message)
            
            grid_search_cv.fit(input_feature, output_feature)
            message = f'{">>"*30} f"Training {type(initialized_model.model).__name__} Completed." {"<<"*30}'
            grid_searched_best_model = GridSearchedBestModel(model_serial_number=initialized_model.model_serial_number,
                                                             model=initialized_model.model,
                                                             best_model=grid_search_cv.best_estimator_,
                                                             best_parameters=grid_search_cv.best_params_,
                                                             best_score=grid_search_cv.best_score_)
            
            return grid_searched_best_model            
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    def get_initialized_model_list(self):
        try:
            initialized_model_list = []
            for model_serial_number in self.model_initialization_config.keys():
                model_initialization_config = self.model_initialization_config[model_serial_number]
                model_obj_ref = ModelFactory.class_for_name(module_name=model_initialization_config[MODULE_KEY],
                                                            class_name=model_initialization_config[CLASS_KEY])
                model = model_obj_ref()
                
                if PARAM_KEY in model_initialization_config:
                    model_obj_property_data =dict(model_initialization_config[PARAM_KEY])
                    model = ModelFactory.update_property_of_class(instance_ref=model,
                                                                  property_data=model_obj_property_data)
                param_grid_search = model_initialization_config[SEARCH_PARAM_GRID_KEY]
                model_name = f"{model_initialization_config[MODULE_KEY]}.{model_initialization_config[CLASS_KEY]}"
                
                model_initialization_config = InitializedModelDetail(model_serial_number=model_serial_number,
                                                                     model=model,
                                                                     param_grid_search=param_grid_search,
                                                                     model_name=model_name)
                initialized_model_list.append(model_initialization_config)
            self.initialized_model_list = initialized_model_list
            return self.initialized_model_list                
        except Exception as e:
            raise HousingException(e, sys) from e
        
    def initiate_best_parameter_search_for_initialized_model(self, initialized_model,input_feature,
                                                             output_feature):     
        try:
            return self.execute_grid_search_operation(initialized_model=initialized_model,
                                                      input_feature=input_feature,
                                                      output_feature=output_feature)
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    def initiate_best_parameter_search_for_initialized_models(self,initialized_model_list,
                                                              input_feature,output_feature):
        try:
            self.grid_searched_best_model_list = []
            for initialized_model_list in initialized_model_list:
                grid_searched_best_model=self.initiate_best_parameter_search_for_initialized_model(
                    initialized_model=initialized_model_list,
                    input_feature=input_feature,
                    output_feature=output_feature
                )
                self.grid_searched_best_model_list.append(grid_searched_best_model)
            return self.grid_searched_best_model_list
        except Exception as e:
            raise HousingException(e, sys) from e
        
        
    @staticmethod
    def get_model_detail(model_details,model_serial_number):
        try:
            for model_data in model_details:
                if model_data.model_serial_number == model_serial_number:
                    return model_data
        except Exception as e:
            raise HousingException(e, sys) from e
        
    
    @staticmethod
    def get_best_model_from_grid_searched_best_model_list(grid_searched_best_model_list,
                                                          base_accuracy=0.6):
        
        try:
            best_model = None
            for grid_searched_best_model in grid_searched_best_model_list:
                if base_accuracy < grid_searched_best_model.best_score:
                    logging.info(f"Acceptable model found: {grid_searched_best_model} ")
                    base_accuracy = grid_searched_best_model.best_score
                    
                    best_model = grid_searched_best_model
            if not best_model:
                raise Exception(f"None of Model has basee accuracy: {base_accuracy}")
            logging.info(f"Best model: {best_model}")
            return best_model
        except Exception as e:
            raise HousingException(e, sys) from e
        
    
    def get_best_model(self, X,y, base_accuracy=0.6):
        try:
            logging.info("Starteed Initializing model from config file")
            initialized_model_list = self.get_initialized_model_list()
            logging.info(f"Initialized model: {initialized_model_list}")
            grid_searched_best_model_list =self.initiate_best_parameter_search_for_initialized_models(
                initialized_model_list=initialized_model_list,
                input_feature=X,
                output_feature=y
            )
            return ModelFactory.get_best_model_from_grid_searched_best_model_list(grid_searched_best_model_list,
                                                                                  base_accuracy= base_accuracy)
        except Exception as e:
            raise HousingException(e, sys) from e