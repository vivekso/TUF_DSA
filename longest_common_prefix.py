class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ''
        prefix = strs[0]
        for s in strs[1:]:
            while s.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ''
        return prefix

# --- Example Usage ---
if __name__ == "__main__":
    solver = Solution()
    
    # Example 1
    words = ["flower", "flow", "flight"]
    print("Input:", words)
    print("Output:", solver.longestCommonPrefix(words))
    
    # Example 2
    words2 = ["dog", "racecar", "car"]
    print("\nInput:", words2)
    print("Output:", solver.longestCommonPrefix(words2))