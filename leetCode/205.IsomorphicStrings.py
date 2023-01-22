class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t, t_to_s, n = {}, {}, len(s)
        
        for i in range(n):
            if s[i] in s_to_t and s_to_t[s[i]] != t[i]:
                return False
            elif t[i] in t_to_s and t_to_s[t[i]] != s[i]:
                return False
            s_to_t[s[i]] = t[i]
            t_to_s[t[i]] = s[i]
        
        return True

sol = Solution()
sol.isIsomorphic("egg", "add")
sol.isIsomorphic("foo", "bar")
sol.isIsomorphic("paper", "title")