from crypt import methods
from flask import Flask, flash,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from config import config
import requests,os
from cloud import get_sensordata
from cropPrediction import get_prediction
from disease import get_disease

from openWeather import *


UPLOAD_FOLDER = 'static/img/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

slider = [
    {'src':'https://cdn.pixabay.com/photo/2017/06/11/02/05/wheat-2391348_960_720.jpg'},
    {'src':'https://cdn.pixabay.com/photo/2017/06/11/02/05/wheat-2391348_960_720.jpg'}
]

sensor_data = get_sensordata()['data']

pred_crop = None

@app.route('/crop-recommendation')
def recommed_crop():
    if not os.path.exists('static/recommend.txt'):
        pred_crop = get_prediction()['prediction']
        with open('recommend.txt', 'w') as f:
            f.write(pred_crop)
    else:
        with open('recommend.txt') as f:
            pred_crop = f.readlines[0]
    return render_template('index.html',posts=[slider,weather,pred_crop,sensor_data])


weather = get_weather("8aa59ea88fa14d34cb933f68a151157b",16.7907012,80.8476103)
forecast = get_forecast("8aa59ea88fa14d34cb933f68a151157b",16.7907012,80.8476103)

@app.route('/')
def index():
   return render_template('index.html',posts=[slider,weather,pred_crop,sensor_data])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader',methods=['POST','GET'])
def uploader():
    filename = None
    error = None
    if request.method == 'POST':
        if 'file' not in request.files:
            print("Error")
            error = "File not selected"
            return render_template('prediction.html',posts=[error])
        file = request.files['file']
        filename = file.filename
        select = request.form.get('type')
        print(filename)
        if filename == '':
            error = "Filename is empty"
            return render_template('prediction.html',posts=[error]) 

        if allowed_file(filename) == False:
            error = "This file isn't allowed"
            return render_template('prediction.html',posts=[error]) 
        file.save(os.path.join(os.getcwd()+"/static/img/uploads/",filename))
    disease_data = get_disease(filename,select)
    print('!!!!!!!!!!!!!!!!!!!!!!')
    print(select)
    print(disease_data)
    print('!!!!!!!!!!!!!!!!!!!!!!')
    filepath = os.path.join("/static/img/uploads/",filename)
    return render_template('prediction.html',posts=[error,filepath,disease_data,select])

@app.route('/disease-prediction',methods=['POST','GET'])
def disease_prediction():
    return render_template('prediction.html',posts=[])

if __name__ == "__main__":
    app.run(debug=True)