import base64
import json                    
import requests
import os

api = 'https://disease-prediction.azurewebsites.net/plant/disease_prediction'

def get_disease(image_file,plantName):
    img = os.path.join(os.getcwd()+"/static/img/uploads/",image_file)
    # print('!!!!!!!!')
    # print(img)
    # print('!!!!!!!!')
    with open(img, "rb") as f:
        im_bytes = f.read()        
    im_b64 = base64.b64encode(im_bytes).decode("utf8")

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps({"image": im_b64, "plant_name": plantName})
    response = requests.post(api, data=payload, headers=headers)
    # print("im")
    try:
        data = response.json()     
        # print(data)
        return data
        # print("#######################################################")

    except requests.exceptions.RequestException:
        print(response.text)

