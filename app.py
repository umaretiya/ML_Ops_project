from cmath import log
import flask
import sys,os,json,base64
import pandas as pd,numpy as np, matplotlib.pyplot as plt

from sklearn.svm import SVC
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
from io import BytesIO
import seaborn as sns

from housing.logger import logging
from flask import Flask,render_template,send_file,abort,request
from housing.exception import HousingException
from housing.logger import get_log_dataframe 

from housing.util.util import read_yaml_file,write_yaml_file
from housing.config.configuration import Configuration
from housing.constant import CONFIG_DIR,get_current_time_stamp
from housing.pipeline.pipeline import Pipeline
from housing.entity.housing_predictor import HousingPredictor, HousingData
from matplotlib.style import context


ROOT_DIR = os.getcwd()
LOG_FOLDER_NAME = "logs"
PIPELINE_FOLDER_NAME= "housing"
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,"model.yaml")
LOG_DIR = os.path.join(ROOT_DIR,LOG_FOLDER_NAME)
PIPELINE_DIR = os.path.join(ROOT_DIR,PIPELINE_FOLDER_NAME)
MODEL_DIR = os.path.join(ROOT_DIR,SAVED_MODELS_DIR_NAME)

HOUSING_DATA_KEY = "housing_data"
MEDIAN_HOUSING_VALUE_KEY = "median_house_value"


app = Flask(__name__)
app.secret_key = "regression project seret key"

@app.route('/',methods=['GET','POST'])
def index():
    try:
        #collecting a data from local dir
        dataset = "D:\\iNeuron\internship_projects\\Credit Card Default Prediction"
        file_name = "UCI_Credit_Card.csv"
        cwd = os.getcwd()
        file_path = os.path.join(cwd,dataset,file_name)
        # Loding data sets and cleaning ,eda etc
        df = pd.read_csv(file_path)
        df.drop(labels=['ID'],axis=1, inplace=True)
        # Feature selection, lables and traget variables
        X = df.drop(labels=['default.payment.next.month'], axis=1)
        y = df['default.payment.next.month']
        # Train test spliting
        X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3, random_state=42)
        # Model initalizing
        svc = SVC()
        svc.fit(X_train,y_train)
        y_pred = svc.predict(X_test)
        # model accuracy testing
        acc = accuracy_score(y_pred,y_test)
        cm = confusion_matrix(y_pred,y_test)
        data = {"accuracy":acc,"confusion_metrics":cm}
        logging.info("Model accuracy test function")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("main app function is running")
    return render_template("index.html",data=data)

@app.route("/ops")
def project_strating():
    data={"Model":"Classifcaitons","Data":"Housing","sector":"realestate"}
    return render_template("ops.html", context=data)


@app.route('/artifact', defaults={'req_path':'housing'})
@app.route('/artifact/<path:req_path>')
def render_artifact_dir(req_path):
    return render_template("files.html")


@app.route('/view_experiment_hist',methods=['GET','POST'])
def view_experiment_history():
    experiment_df = Pipeline.get_experiments_status()
    context = {
        "experiment":experiment_df.to_html(classes="table table-striped col-12")
    }
    return render_template("experiment_history.html", context=context)


@app.route('/train',methods=['GET','POST'])
def train():
    return render_template("train.html")


@app.route('/predict',methods=['GET','POST'])
def predict():
    return render_template("predict.html")


@app.route('/saved_models', defaults={'req_path':'saved_models'})
@app.route('/saved_models/<path:req_path>')
def saved_models_dir(req_path):
    return render_template("saved_models_files.html")


@app.route("/update_model_config", methods=['GET','POST'])
def update_model_config():
    try:
        return render_template("update_model.html")
    except Exception as e:
        logging.exception(e)
        return str(e)
    
    
@app.route(f'/logs', defaults={'req_path':f'{LOG_FOLDER_NAME}'})
@app.route(f'/{LOG_FOLDER_NAME}/<path:req_path>')
def render_log_dir(req_path):
    return render_template("log_files.html")
    
    
if __name__ == '__main__':
    app.run(debug=True)