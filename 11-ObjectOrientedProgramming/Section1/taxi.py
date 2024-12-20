class TaxiRide:
    def __init__(self, rate_per_km):
        self.rate_per_km = rate_per_km # value in € (e.g. €2)
        self.distance = 0
        self.fare = 0

    def calculate_fare(self, distance):
        self.distance = distance
        self.fare = self.distance * self.rate_per_km

    def print_reciept():
        print('Distance:', self.distance, 'Rate:', self.rate_per_km, 'Fare:',self.fare)

def main():
    # your program
    rides = []
    rides.append(TaxiRide(5))# regular ride
    rides.append(TaxiRide(7.5))# Deluxe ride

    for ride in rides:
        print(ride)

if __name__ == "__main__":
    main()
