def time_string(hours, minutes, time_format):
    if time_format == 24:
        return f'{hours}:{minutes}'
    elif time_format == 12:
        if(hours >= 12):
            m = 'pm'
        else:
            m = 'am'
        return f'{hours}:{minutes}{m}'
    else: return 'Incorrect format'

print('24-hour: ', time_string(11, 42, 24))
print('12-hour: ', time_string(11, 42, 12))