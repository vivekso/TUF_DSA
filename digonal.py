arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]


def diagonalDifference(arr):
    # Write your code here
    f_sum = 0
    b_sum = 0
    length = len(arr)
    for i in range(length):
        # if (i+(i-length))% 2 == 0:
        f_sum += arr[i][i-length]
        b_sum += arr[i][length-i -1]
        print(f_sum,b_sum)
    return(abs(f_sum - b_sum))
print(arr)
print(diagonalDifference(arr))