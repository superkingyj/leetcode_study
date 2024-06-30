from collections import defaultdict
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_logs = defaultdict(set)
        
        for u, t in logs:
            user_logs[u].add(t)
        
        result = [0 for _ in range(k)]
        
        for value in user_logs.values():
            result[len(value)-1] +=1
        
        return result