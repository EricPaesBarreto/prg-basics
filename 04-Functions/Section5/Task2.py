def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_in(n):
    return n // 2.54

def ft_in_to_cm(fe, inch):
    return  30.48 * fe + 2.54 * inch

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f'632cm = {cm_to_in(632)}inches')
    print(f'5ft 11in = {ft_in_to_cm(5, 11)}')

#convert centimeters to inches
#convert feet and inches to centimeters