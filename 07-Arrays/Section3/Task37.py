def transpose(matrix):
    rows = len(matrix)
    columns = len(matrix[0])

    #generate empty 2-d array
    result = []
    for index in range(columns):
        temp_row = [0] * rows
        result.append(temp_row)
        
    #result[i][j] = matrix[j][i]
    for row in range(rows):
        for column in range(columns):
            result[column][row] = matrix[row][column]
    return result

if __name__ == "__main__":
    mat1 = [[1,2,3],
            [4,5,6],
            [7,8,9]]
    result=(transpose(mat1))
    for row in result:
        print(row)
    # expected output
    # [1,4,7]
    # [2,5,8]
    # [3,6,9]
    #revieved output:
    # expected output
    # [7,8,9]
    # [7,8,9]
    # [7,8,9]