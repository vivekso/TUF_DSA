from typing import List
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur_num = {}
        for i in arr:
            if i in occur_num:
                occur_num[i] += 1
            else:
                occur_num[i] = 1
        occurrences = list(occur_num.values())
        return type(occur_num)

        for j in range(len(occurrences) - 1):
            for k in range(j + 1, len(occurrences)):
                if occurrences[j] == occurrences[k]:
                    return False
        return True
arr = [1, 2, 2, 1, 1, 3]
sol = Solution()
result = sol.uniqueOccurrences(arr)
print(result)