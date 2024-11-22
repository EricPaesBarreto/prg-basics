categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
largest = expenses[0]
largest_index = 0
for index in range(len(expenses)):
    if expenses[index] > largest:
        largest_index = index
print(categories[largest_index])