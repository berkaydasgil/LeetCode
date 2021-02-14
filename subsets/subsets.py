class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 : return []
        
        result = [[]]
        
        for i in nums:
            result += [list + [i] for list in result]
        return result
        