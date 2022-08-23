class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        
        def backtracking(choosed, idx):
            if sum(choosed) == target:
                if choosed not in result:
                    result.append(choosed)
                return

            if idx >= len(candidates): return

            for i in range(idx, len(candidates)):
                if sum(choosed)+candidates[i] <= target:
                    backtracking(choosed+[candidates[i]], i)       
                    backtracking(choosed+[candidates[i]], i+1)
        
        backtracking([], 0)
        return result
