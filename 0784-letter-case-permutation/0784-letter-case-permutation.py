class Solution:
    def backtracking(self, idx, new_s):
        if idx == self.l:
            self.result.append(new_s)
            return
        
        self.backtracking(idx+1, new_s+self.s[idx])
        if self.s[idx].isalpha():
            self.backtracking(idx+1, new_s+self.s[idx].upper())
        
        
    def letterCasePermutation(self, s: str) -> List[str]:
        self.l = len(s)
        self.result = []
        self.s = s.lower()
        self.backtracking(0, "")
        return self.result