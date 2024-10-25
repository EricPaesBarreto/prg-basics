fn = 0
f1 = 0
f2 = 1
for i in range(21):
    print(fn)
    fn = f1 + f2
    f2 = f1
    f1 = fn