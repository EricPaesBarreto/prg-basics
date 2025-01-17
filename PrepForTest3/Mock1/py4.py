fnc1 = lambda x: "id:"+x[:2] # first two
fnc2 = lambda x: (x[0]+x[-1]).upper() # first and last
# fnc2 "WR,CE,TO"

def f(fnc, inp):
    return ",".join(list(map(fnc,inp)))

if __name__ == "__main__":
    prods = ["water","cheese","tomato"] 
    print(f(fnc1,prods))
    print(f(fnc2,prods))