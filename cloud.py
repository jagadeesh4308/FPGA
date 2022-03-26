from unicodedata import name
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from config import config
import requests

connect_str = config.database

blob_service_client = BlobServiceClient.from_connection_string(connect_str)

container1 = "image"
container2 = "sensordata"

container1_client = blob_service_client.get_container_client(container=container1)
container2_client = blob_service_client.get_container_client(container=container2)

def get_sensordata():

    try:
        blob_client = container2_client.get_blob_client(blob='sensor.json')
        # print()
        response = requests.get(blob_client.url).json()
        print(response)
        return response
    except Exception as e:
        return e

        
