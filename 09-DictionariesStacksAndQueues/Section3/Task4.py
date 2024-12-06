import queue

def dec_to_bin(input):
    stack = queue.LifoQueue()
    while input > 0:
        if input % 2 == 0:
            stack.put("0")
        else:
            stack.put("1")
        input = int(input/2)
    result = ""
    while not stack.empty():
        result += stack.get()
    return result

if __name__ == "__main__":
    num = input("Enter a natural number: ")
    print("Natural number:",num,"\n Binary number:",dec_to_bin(int(num)))