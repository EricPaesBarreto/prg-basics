def sum_digeo(number, even):
    str_num = str(number)
    result = 0
    if even:
        for digit in str_num:
            if(int(digit)%2==0):
                result+=int(digit)
    else:
        for digit in str_num:
            if(int(digit)%2!=0):
                result+=int(digit)
    return result

nums = [3124, 3124, 20576, 20576, 13115]
bools = [True, False, False, True, True]

for i in range(0,5):
    print(sum_digeo(nums[i], bools[i]))