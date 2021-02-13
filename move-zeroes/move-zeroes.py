class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        lastzeroindex = 0
        for i in range(len(nums)):
            if nums[i] is not 0:
                nums[i], nums[lastzeroindex] = nums[lastzeroindex], nums[i]
                lastzeroindex+=1
