def twoSum(numbers, target):
    i = 0
    j = len(numbers)-1
    arr_sum = 0
    while (i< j):
        arr_sum = numbers[i]+numbers[j]
        if arr_sum < target:
            i +=1
        elif arr_sum > target:
            j -=1
        else :
            return [i+1,j+1]
    return -1

arr = [2,7,11,15]
target = 20
print(twoSum(arr,target))