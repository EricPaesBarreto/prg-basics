import matplotlib.pyplot as plt
Recordings = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}

cities = list(Recordings.keys())
Temperatures = list(Recordings.Values())

plt.bar(cities, Temperatures)

plt.title("Temperatures recorded in cities")
plt.xlabel("Cities")
plt.ylabel("Temperatures (°C)")

plt.show()