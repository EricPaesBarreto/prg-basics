# Sample data
temps = {"Krakow": 7, "Warszawa": -2, "Sopot": 4, "Koszalin": -1, "Opole": 3}

# define function to check if city temp is positive
is_positive = lambda number: number[1] > 1

# find positive temp cities
positive_temps = filter(is_positive, temps.items())

# get name function
get_name = lambda item: item[0]

# get names only
positive_cities = map(get_name, positive_temps)

# list the names of all positive cities
print('Cities with positive temperatures:'," ".join(positive_cities))