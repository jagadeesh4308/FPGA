import requests
import json
from cloud import get_sensordata,get_rfsdata

api = r'https://crop-recommendation.azurewebsites.net/plant/crop_recommendation'

res = get_sensordata()
res2 = get_rfsdata()

def get_prediction():
    data = {
        "data": {
            'N': float(res['Nitro']),
            'P': float(res['Phosp']),
            'K': float(res['Potas']), 
            'temperature': res2['temperature'], 
            'humidity': res2['humidity'],
            'ph': float(res['pH'])
            }
        }

    #print(data)

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps(data)

    response = requests.post(api, data=payload, headers=headers)
    try:
        data = response.json()     
        return data              
    except requests.exceptions.RequestException:
        print(response.text)


# prediction = requests.post(url, data = data)

# print(prediction)

get_prediction()

