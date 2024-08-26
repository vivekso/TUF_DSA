nums = [-4,-1,0,3,10]
print(nums)
def sortedSquares(arr):
    sqr_arr = []
    for i in range(len(arr)):
        print(range(len(arr)))
        n = arr[i]*arr[i]
        print("sqr number",n)
        sqr_arr.append(n)
    return (sorted(sqr_arr))

print('sorted array ',sortedSquares(nums))