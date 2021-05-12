class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        sum = 0
        for element in nums:
    
            runningSum.append(sum+element)
            sum += element
        return runningSum
            