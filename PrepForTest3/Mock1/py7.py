def f(matrix):
    collumn_sum = [0 for i in range(len(matrix[0]))]

    # count sums
    for i_hat in range(len(matrix)):
        # row
        for j_hat in range(len(matrix[0])): # assume all rows are same length
            # column
            collumn_sum[j_hat] += matrix[i_hat][j_hat]
    
    # are at least two sums identical
    for index in range(len(collumn_sum)):
        for index_2 in range(len(collumn_sum)):
            if index == index_2: continue
            if collumn_sum[index] == collumn_sum[index_2]: return True
    return False

if __name__ == "__main__":
    print(f([[3,4,2],[5,1,6]]))
    print(f([[3,4,2],[5,1,7]]))
    print(f([[3,4],[5,1],[4,7]]))
    print(f([[3,4],[5,9],[4,7]]))