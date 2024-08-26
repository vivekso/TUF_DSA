arr = [-4, 3, -9, 0, 4, 1]
def plusMinus(arr):
    # Write your code here
    positive_count = 0
    negative_count = 0
    zero_count = 0
    arr_length = len(arr)
    for i in arr:
        if i > 0:
            positive_count += 1
        elif i < 0:
            negative_count += 1
        else:
            zero_count += 1
    return(round(positive_count/arr_length,6),round(negative_count/arr_length,6),round(zero_count/arr_length,6))

# print(plusMinus(arr))

def staircase(n):
    # Write your code here
    for i in range(1,n+1):
        print(' '*(n-i)+'#'*i)
print(staircase(6))