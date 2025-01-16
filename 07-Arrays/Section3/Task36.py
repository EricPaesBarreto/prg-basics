def identity(size):
    result = [[0 for _ in range(size)] for _ in range(size)]
    for index in range(size):
        result[index][index] = 1
    return result

if __name__ == "__main__":
    identity_matrix = identity(5)
    for row in identity_matrix:
        print(row)