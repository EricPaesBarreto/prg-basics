def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

if __name__ == "__main__":
    print(bubbleSort([7,4,8,45,3,7,9,5,90,36,37,16]))