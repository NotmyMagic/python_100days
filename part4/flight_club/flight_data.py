IATA_ENDPOINT = "https://test.api.amadeus.com/v1/reference-data/shopping/flight-offers"

class FlightData:
    #This class is responsible for structuring the flight data.
    
    def __init__(self, price, origin_airport, destination_airport, departure_date):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date

def find_cheapest_flight(data):
    if data is None or not data["data"]:
        print("no flight data")
        return FlightData("N/A","N/A","N/A","N/A")
    
    first_flight = data["data"][0]
    lowest_price = float(first_flight["price"]["grandTotal"])
    origin = first_flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
    destination = first_flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
    departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]

    cheapest_flight = FlightData(lowest_price, origin, destination, departure_date)
    
    for flight in data["data"]:
        price = float(flight["price"]["grandTotal"])
        if price < lowest_price:
            lowest_price = price
            origin = flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]
            destination = flight["itineraries"][0]["segments"][0]["arrival"]["iataCode"]
            departure_date = first_flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, departure_date)
            print(f"lowest_price to {destination} is {lowest_price}")
        
    return cheapest_flight