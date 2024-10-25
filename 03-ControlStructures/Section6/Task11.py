current_price = 140
previous_price = 200
difference = (previous_price - current_price) / previous_price
change = int((difference)*100)
if difference <= 0.9:
    print(f'Buy the product!\nProduct price reduced by {change}%')