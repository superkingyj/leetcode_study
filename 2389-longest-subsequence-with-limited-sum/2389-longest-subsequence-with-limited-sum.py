class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        l = len(nums)
        nums.sort()
        result = []
        
        for query in queries:
            if query < nums[0]:
                result.append(0)
                continue
                
            sum_val, idx = nums[0], 0
            while True:
                if idx+1 < l and sum_val + nums[idx+1] <= query:
                    sum_val += nums[idx+1]
                    idx += 1
                else:
                    break
            
            result.append(idx+1)
        
        return result
            