#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import time
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
# print(sheet_data.response.text)
flight_search = FlightSearch()


ORIGIN_CITY_IATA = "LON"


for row in sheet_data:
    if row["iataCode"] == "":
        row["iataCode"] = flight_search.get_destination_code(row["city"])
        time.sleep(2)
print(f"sheet_data: \n {sheet_data}")

data_manager.destination_data = sheet_data
data_manager.update_destination_codes()


tomorrow = datetime.now() + timedelta(days=1)
two_month_from_today = datetime.now() + timedelta(days=(2*30))

for destination in sheet_data:
    print(f"Getting flights for {destination["city"]}...")
    flights = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        departure_date=tomorrow,
    )
    cheapest_flight = find_cheapest_flight(flights)
    print(f"{destination["city"]}: {cheapest_flight.price}")
    time.sleep(2)