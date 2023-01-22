class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # Test case 
        # ["abc", "ab", "abcd"] --> "ab"
        
        # Time Complexity -> O(N^2)
        # Space Complexity -> O(1)
        
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][0:i]
                
        return strs[0]