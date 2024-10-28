def neg_even(x, y):
    count = 0
    for i in range(x, y+1):
        if i < 0 and i % 2 == 0:
            count+=1
    return count
    
#test

print(neg_even(-7, 8))
print(neg_even(-1, 11))