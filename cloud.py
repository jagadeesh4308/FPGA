from unicodedata import name
from urllib import response
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import config
import requests
import os,shutil

connect_str = config.database

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container1 = "image"
container2 = "sensordata"
container3 = "rfsdata"

container1_client = blob_service_client.get_container_client(container=container1)
container2_client = blob_service_client.get_container_client(container=container2)
container3_client = blob_service_client.get_container_client(container=container3)

def get_sensordata():

    try:
        blob_client = container2_client.get_blob_client(blob='sensor.json')
        # print()
        response = requests.get(blob_client.url).json()
        #print(response)
        return response
    except Exception as e:
        return e

def get_rfsdata():

    try:
        blob_client = container3_client.get_blob_client(blob='rfsdata.json')
        # print()
        response = requests.get(blob_client.url).json()
        #print(response)
        return response
    except Exception as e:
        return e

def get_imagedata():

    try:
        blob_client = container1_client.get_blob_client(blob='crop.jpg')
        c = len(os.listdir('static/img/downloads'))

        file_name = f"static/img/downloads/{c}.jpg"

        res = requests.get(blob_client.url, stream = True)

        if res.status_code == 200:
            with open(file_name,'wb') as f:
                shutil.copyfileobj(res.raw, f)
            #print('Image sucessfully Downloaded: ',file_name)
        else:
            print('Image Couldn\'t be retrieved')
        return sorted(os.listdir('static/img/downloads'),key=lambda x: int(x.split(".")[0]))
    except Exception as e:
        return e


        
