def f(ids):
    for i in range(len(ids)):
        for j in range(len(ids)):
            if i == j: continue
            if ids[i] == ids[j]: return False
    return True

if __name__ == "__main__":
    print(f(["john5","ann123","JOHN5","xxx","abc333","a10"]))
    print(f(["abc123","ann","abc123","a10"]))
    print(f(["bob2","bob2"]))
    print(f(["bob2","BOB2"]))