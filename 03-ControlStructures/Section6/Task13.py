speed = int(input('Enter car speed: '))
speed_limit_min = 40
speed_limit_max = 140
if speed >= speed_limit_min and speed <= speed_limit_max:
    print('Good speed.')
elif speed < speed_limit_min:
    print('Too slow!')
else:
    print('Too fast!')