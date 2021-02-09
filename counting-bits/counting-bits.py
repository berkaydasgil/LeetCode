class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        dp[0]=0
        j=1
        for i in range(1,num+1):
            while i - 2 ** j > 0:
                j+=1
            if i - 2**j == 0: 
                dp[i]=1
                continue
            dp[i]=1+dp[i-2**(j-1)]
        return dp
            
