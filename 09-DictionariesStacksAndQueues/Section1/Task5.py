countries = [
{"name":"Poland", "population":38000000},
{"name":"Brazil", "population":216400000},
{"name":"China", "population":1411000000},
{"name":"Pakistan", "population":240500000},
{"name":"Mozambique", "population":33900000}
]

print("COUNTRY POPULATION")

for country in countries:
    print(country["name"],":",country["population"])