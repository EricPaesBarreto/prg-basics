price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}

full_total=0
reduced_total=0

print("Before discount:")
for item,price in price_list.items():
    full_total+=price
    print(item,":",price)

print("\nAfter discount:")
for item,price in price_list.items():
    reduced_price = round(price*(9/10),2)
    reduced_total += reduced_price
    print(item,":",reduced_price)

print("\nTotal price of all items:\n")

print("Before discount:",round(full_total,2),"\After discount:",round(reduced_total,2))