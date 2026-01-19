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
    
    '''
        Why this is optimal

        Time Complexity: O(n) (single pass)

        Space Complexity: O(1) (no extra data structures)

        No unnecessary slicing

        Returns the true longest subarray

        Works perfectly for positive integers
    '''

    def longestSubArray(self):
        left = 0
        current_sum = 0
        max_len = 0
        start = -1

        for right in range(len(self.arr)):
            current_sum += self.arr[right]

            while current_sum > self.target:
                current_sum -= self.arr[left]
                left += 1

            if current_sum == self.target:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    start = left

        return self.arr[start:start + max_len] if start != -1 else []

    

nums = [1, 2, 3, 1, 1, 1, 1]
target = 3

obj = Longest_Subarray_with_given_Sum_K_Positives(nums, target)
# print(obj.longestSubArray())
print(obj.longestSubArray())