import sys

def dp(nums):
    n = len(nums)

    if n <= 2: return sum(nums)

    dp = [0] * (n+1)
    dp[1] = nums[0]
    dp[2] = nums[0] + nums[1]
    dp[3] = max(nums[0], nums[1]) + nums[2]

    for i in range(4, n+1):
        dp[i] = max(dp[i-2], dp[i-3]+nums[i-2]) + nums[i-1]
        print(dp[i])
    
    return dp[-1]


T = int(sys.stdin.readline())
nums = []
for _ in range(T):
    nums.append(int(sys.stdin.readline()))
print(dp(nums))