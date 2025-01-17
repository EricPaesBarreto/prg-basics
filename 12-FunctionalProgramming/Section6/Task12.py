def f(data):
    

if __name__ == "__main__":
    data = [508,500,512,499,492,511,503,476,501,509]
    print("Bottle capacity:    500ml")
    print("Filling tolerance:  2%")
    print(f"Filled bottles:     {data}")
    incorrectly_filling = f(data)
    print(f"Incorrectly filled: {incorrectly_filled}%")