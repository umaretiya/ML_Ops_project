import flask
import sys
from housing.logger import logging
from flask import Flask,render_template
from housing.exception import HousingException

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testin custom exception")
    except Exception as e:
        housing = HousingException(e,sys)
        logging.info(housing.error_message)
        logging.info("main app function is running")
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)