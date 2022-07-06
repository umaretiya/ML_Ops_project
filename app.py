from crypt import methods
import flask

from flask import Flask,render_template

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    return "<h1>Hello Flask with Docker</h1>"

if __name__ == '__main__':
    app.run(debug=True,port = 5000)