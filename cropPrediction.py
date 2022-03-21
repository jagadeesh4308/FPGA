import requests
import json
from cloud import get_sensordata

api = r'https://crop-recommendation.azurewebsites.net/plant/crop_recommendation'

res = get_sensordata()['data']
# print(res)

def get_prediction():
    data = {
        "data": {
            'N': res['Nitrogen'],
            'P': res['Phosporus'],
            'K': res['Pottasium'], 
            'temperature': res['Temperature (°C)'], 
            'humidity': res['Humidity'],
            'ph': res['pH']
            }
        }

    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    
    payload = json.dumps(data)
    response = requests.post(api, data=payload, headers=headers)
    try:
        data = response.json()     
        # print(data)  
        return data              
    except requests.exceptions.RequestException:
        print(response.text)


# prediction = requests.post(url, data = data)

# print(prediction)
