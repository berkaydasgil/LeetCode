## Silmene gerek yok sonucu, time limite takiliyor, cok fazla cozme yontemi var bunu solutionlarda bir ara gelbunu calis.

class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2: return 1 if n == 1 else 0
        
        dp = [0] * (n+1)
        dp[0]=1
        dp[1]=1
        
        for i in range(2,n+1):
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]
        
        
    