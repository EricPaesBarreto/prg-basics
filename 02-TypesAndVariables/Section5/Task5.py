price = float(input("Please enter a price: "))
discount = float(input("Please enter a discount (%): "))
w_discount = round((price - (price * (discount/100))), 2)
reduction = round((price-w_discount), 2)
print(f"Price with discound: {w_discount}, reduction: {reduction}.")