import requests
import json
from pprint import pprint
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

API_KEY = os.getenv("plants_api") # Your API_KEY here
PROJECT = "all"  # try specific floras: "weurope", "canada"…
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}"

image_path_1 = "mango.jpg"
image_data_1 = open(image_path_1, 'rb')

data = {'organs': ['leaf']}

files = [
    ('images', (image_path_1, image_data_1))
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

pprint(response.status_code)
pprint(json_result)

