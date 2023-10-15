class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: 
            return None
        n = len(nums)
        last = right = 0
        while right<n:
            if nums[right]!=0:
                nums[last],nums[right] = nums[right],nums[last]
                last+=1
            right+=1
        return last
