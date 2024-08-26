def rotate(nums,k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        # print(nums)
        ele = nums[-1]
        # nums.append(nums[-1])
        # print(nums)
        nums.pop()
        print("delete ele",nums)
        nums.append(ele)

    return nums
nums = [1,2,3,4,5,6,7]
k = 3
print(rotate(nums, k))