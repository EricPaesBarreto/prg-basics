def squash_matrix(matrix):
    result = []
    for row in matrix:
        for item in row:
            result.append(item)
    return result

if __name__ == "__main__":
    mat1 = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    print(squash_matrix(mat1))