from crypt import methods
import json
from flask import Flask, flash,render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from config import config
import requests,os
from cloud import get_sensordata,get_imagedata,get_rfsdata
from cropPrediction import get_prediction
from disease import get_disease
from datetime import date
from datetime import datetime
from openWeather import *


UPLOAD_FOLDER = 'static/img/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

slider1 = get_imagedata()
slider = []
#print(slider)
if(len(slider1)>5):
    for i in range(5):
        slider.append(slider1[i])

else:
    slider = slider1

#print(slider)
    


sensor_data = get_sensordata()
rfs = get_rfsdata()
fertilizers_data = json.load(open('fertilizersnew.json'))

days_count = None
phaseName = None
phaseData = None

if not os.path.exists('register.txt'):
        with open('register.txt', 'w') as f:
            f.write(str(date.today()))
else:
    with open('register.txt') as f:
        fetch_start = f.readlines()[0]
        start = datetime.strptime(fetch_start, '%Y-%m-%d').date()
        days_count = (start - date.today()).days * -1
        # print(days_count)
        if(days_count>=1 and days_count<=25):
            phaseName = 'Mid-Tillering'
            phaseData = fertilizers_data['Mid-Tillering']
        elif(days_count>=25 and days_count<=27):
            phaseName = 'Maximum-Tillering'
            phaseData = fertilizers_data['Maximum-Tillering']
            # elif(days_count>=28 and days_count<=29):
            #     phase = "Panicle-Initiation"
            # elif(days_count>=29 and days_count<=105):
            #     phase = "Flag-Leaf"

# print(phaseName)

    

#print(phaseData)


pred_crop = None
registered_date = None

@app.route('/crop-recommendation')
def recommed_crop():
    if not os.path.exists('recommend.txt'):
        pred_crop = get_prediction()['prediction']
        with open('recommend.txt', 'w') as f:
            f.write(pred_crop)
    else:
        with open('recommend.txt') as f:
            pred_crop = f.readlines()[0]
    return render_template('index.html',posts=[slider,weather,pred_crop,sensor_data,rfs,registered_date,phaseName,phaseData])

@app.route('/crop-register')
def crop_register():
    registered_date = None 
    if not os.path.exists('register.txt'):
        with open('register.txt', 'w') as f:
            f.write(str(date.today()))
    else:
        with open('register.txt') as f:
            registered_date = f.readlines()[0]
    return render_template('index.html',posts=[slider,weather,pred_crop,sensor_data,rfs,registered_date,phaseName,phaseData])


weather = get_weather("8aa59ea88fa14d34cb933f68a151157b",16.7907012,80.8476103)
forecast = get_forecast("8aa59ea88fa14d34cb933f68a151157b",16.7907012,80.8476103)
print(forecast)

@app.route('/')
def index():
   return render_template('index.html',posts=[slider,weather,pred_crop,sensor_data,rfs])

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/uploader',methods=['POST','GET'])
def uploader():
    filename = None
    error = None
    select = None
    if request.method == 'POST':
        if 'file' not in request.files:
            print("Error")
            error = "File not selected"
            return render_template('prediction.html',posts=[error])
        file = request.files['file']
        filename = file.filename
        select = request.form.get('type')
        #print(filename)
        if filename == '':
            error = "Filename is empty"
            return render_template('prediction.html',posts=[error]) 

        if allowed_file(filename) == False:
            error = "This file isn't allowed"
            return render_template('prediction.html',posts=[error]) 
        file.save(os.path.join(os.getcwd()+"/static/img/uploads/",filename))
    if select:
        disease_data = get_disease(filename,select)
    else:
        return render_template('prediction.html',posts=[])
    # print('!!!!!!!!!!!!!!!!!!!!!!')
    # print(select)
    # print(disease_data)
    # print('!!!!!!!!!!!!!!!!!!!!!!')
    filepath = os.path.join("/static/img/uploads/",filename)
    return render_template('prediction.html',posts=[error,filepath,disease_data,select])


@app.route('/disease-prediction',methods=['POST','GET'])
def disease_prediction():
    return render_template('prediction.html',posts=[])

if __name__ == "__main__":
    app.run(debug=True)