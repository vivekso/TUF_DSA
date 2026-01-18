class Longest_Subarray_with_given_Sum_K_Positives:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def longestSubArray(self):
        left = 0
        current_sum = 0

        for right in range(len(self.arr)):
            current_sum += self.arr[right]

            while current_sum > self.target:
                current_sum -= self.arr[left]
                left += 1

            if current_sum == self.target:
                return self.arr[left:right+1]

        return []
    

nums = [10, 5, 2, 7, 1, 9]
target = 14

obj = Longest_Subarray_with_given_Sum_K_Positives(nums, target)
print(obj.longestSubArray())