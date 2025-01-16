def multiplication_table(size):
    table = [[0 for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for column in range(size):
            table[row][column] = (row+1)*(column+1)
    return table

if __name__ == "__main__":
    mTable = multiplication_table(5)
    for row in mTable:
        print(row)