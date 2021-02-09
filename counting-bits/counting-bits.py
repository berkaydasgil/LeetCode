class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0] * (num+1)
        dp[0]=0
        for i in range(1,num+1):
            j=1
            while i - 2 ** j > 0:
                j+=1
            if i - 2**j == 0: 
                dp[i]=1
                continue
            j-=1
            dp[i]=1+dp[i-2**j]
        return dp
            
        # 1 01
        # 2 10
        # 3 11
        # 4 100
        # 5 101
          # 6 110
          # 7 111
          # 8  1000
          # 9 1001 