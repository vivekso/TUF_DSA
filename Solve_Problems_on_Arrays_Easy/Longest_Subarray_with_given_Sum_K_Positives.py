class Longest_Subarray_with_given_Sum_K_Positives:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target

    def longestSubArray(self):
        left = 0
        current_sum = 0
        max_len = 0
        result = []

        for right in range(len(self.arr)):
            current_sum += self.arr[right]

            while current_sum > self.target:
                current_sum -= self.arr[left]
                left += 1

            if current_sum == self.target:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    result = self.arr[left:right+1]

        return result
    

nums = [10, 8, 5, 2, 7, 1, 9]
target = 8

obj = Longest_Subarray_with_given_Sum_K_Positives(nums, target)
print(obj.longestSubArray())