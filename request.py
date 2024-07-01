import requests
import pandas as pd 
from dotenv import load_dotenv
import os

class DataFetch():
    def __init__(self):
        load_dotenv()
        self.url= os.getenv("URL")

    def fetch_data(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            json_request = response.json()
            print(f"successfully fetched data from the URL")
            return json_request
                
        except requests.exceptions.RequestException as e:
            print(f"Unable to connect and status code:{e}")
            return None

    def process_response(self,json_response): 
        if json_response:
            results_json = json_response["results"]
            for attributes in results_json[:3]:
                print(f"Gender: {attributes['gender']}")
        else:
            print(f"Unable to fetch any data")

data_fetcher = DataFetch()
json_response = data_fetcher.fetch_data()
data_fetcher.process_response(json_response) 
