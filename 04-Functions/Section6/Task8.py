def amount_to_pay(num):
    result = 0
    while num > 0:
        if num >= 5:
            num-=5
            result+=1
        elif num >= 2:
            num -=2
            result+=1
        else:
            num-=1
            result+=1
    return result

#tests:
print(amount_to_pay(23))
print(amount_to_pay(8))
print(amount_to_pay(2))
print(amount_to_pay(0))