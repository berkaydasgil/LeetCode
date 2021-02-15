class Solution:
    
    def numberOfMatches(self, n: int) -> int:
        result = 0  

        def backtrack(n,result):
            if n == 0: 
                # print('returned')
                return result  
            if n % 2 == 0 : 
                # print('even')
                n = n/2
                result += n
                return backtrack(n,result)
            else:
                # print('odd')
                n = (n-1)/2
                result+= n
                if n ==0: return result
                else: n+=1
                return backtrack(n,result)
        
        return int(backtrack(n,result))
        
        
                
        