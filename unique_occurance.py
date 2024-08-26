from typing import List
import collections

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        for i, freq in collections.Counter(arr).items():
            if freq in seen:
                return False
            seen.add(freq)
        return True

# Example usage
arr = [1, 2, 2, 1, 1, 3]
sol = Solution()
result = sol.uniqueOccurrences(arr)
print(result)
