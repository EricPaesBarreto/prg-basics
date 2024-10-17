amount = float(input("Please enter an amount: "))
vat = round((amount * 0.23), 2)
total = round((amount + vat), 2)
print(f"price of product: {amount}, VAT: {vat}, total: {total}.")