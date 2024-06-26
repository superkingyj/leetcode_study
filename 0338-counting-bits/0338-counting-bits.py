import math
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        if n == 0: return dp
        
        dp[1] = 1
        
        for i in range(2, n+1):
            if i & i-1 == 0:
                dp[i] = 1
            else:
                biggest_pow_of_2 = 2 ** int(math.log(i, 2))
                dp[i] = dp[i-biggest_pow_of_2]+1
            
        return dp
        
"""
0:00    --> 0
1:01    --> 1
2:10    --> 1 -> 2^1
3:11    --> 2
---------------------
4:100   --> 1 -> 2^2 
5:101   --> 2
6:110   --> 2
7:111   --> 3
---------------------
8:1000  --> 1 -> 2^3 
9:1001  --> 2 -> 2
10:1010 --> 2
11:1011 --> 3
----------------------
12:1100 --> 2
13:1101 --> 3
14:1110 --> 3
15:1111 --> 4
---------------------
16:10000 -> 1
17:10001 -> 2
18:10010 -> 2
19:10011 -> 3
"""