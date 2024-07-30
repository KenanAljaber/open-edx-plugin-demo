import requests
import json


def post(url, data):
    try:
         response=requests.post(url, data=json.dumps(data), headers={'content-type': 'application/json'})
         print(f"data sent: {data}")
         print(f"status code: {response.status_code}")
         response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to send enrollment data: {e}")