person = {
   "name": "Marek",
   "surname": "Banach",
   "age": 25,
   "hobby": ["swimming","excursions"],
   "married": True,
   "phone":{"landline":"123444321","mobile":"777888999"}
}

def print_keys_values(dictionary):
    for key,value in dictionary.items():
        print(key,":",value)

print(person["name"])

print(person["hobby"])

print_keys_values(person)

person["surname"] = "Nowak"

person["married"] = False

person.update({"gender":"male"})

person["hobby"].append("bicycle")

person["phone"].update({"work":"313131444"})

print_keys_values(person)