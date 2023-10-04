class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        last = 0 
        i = 0 
        while i<n:
            if nums[i]!=0:
                nums[last],nums[i] = nums[i], nums[last]
                last+=1
            i+=1
