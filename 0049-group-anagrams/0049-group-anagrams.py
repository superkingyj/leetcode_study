from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_d = defaultdict(list)
        
        for string in strs:
            idx = "".join(sorted(string))
            result_d[idx].append(string)

        return result_d.values()