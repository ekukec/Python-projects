from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/ac39b99b274a047c27d07fd7ce243492/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/ac39b99b274a047c27d07fd7ce243492/flightDeals/users"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_users(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT)
        data = response.json()
        return data["users"]