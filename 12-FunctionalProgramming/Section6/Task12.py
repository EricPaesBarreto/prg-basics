def fits_tolerance(main, tolerance): 
    return lambda data: (data > main - (main * tolerance) and data < main + (main * tolerance))
    

if __name__ == "__main__":
    data = [508,500,512,499,492,511,503,476,501,509]
    print("Bottle capacity:    500ml")
    print("Filling tolerance:  2%")
    print(f"Filled bottles:     {data}")
    correctly_filled = list(filter(fits_tolerance(500, 0.02), data))
    incorrect_percentage = (len(data) - len(correctly_filled)) / len(data) * 100
    print(f"Incorrectly filled: {incorrect_percentage}%")