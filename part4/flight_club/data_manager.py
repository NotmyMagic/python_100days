import os
import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

DATA_ENDPOINT = "https://api.sheety.co/db6218de4ffe5af970b39504f2dd2389/copyOfFlightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.user = os.environ["SHEETY_USERNAME"]
        self.password = os.environ["SHEETY_PASSWORD"]
        self.auth = HTTPBasicAuth(self.user, self.password)
        self.destination_data = {}

        # self.data_endpoint = "https://api.sheety.co/db6218de4ffe5af970b39504f2dd2389/copyOfFlightDeals/prices"
        # self.response = requests.get(url=self.data_endpoint)

    def get_destination_data(self):
        response = requests.get(url=DATA_ENDPOINT, auth=self.auth)
        data = response.json()
        self.destination_data = data["prices"]
        # print(data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{DATA_ENDPOINT}/{city['id']}",
                json=new_data,
                auth=self.auth
            )
            print(response.text)





# response = requests.get(url=data_endpoint)
# print(response.text)
