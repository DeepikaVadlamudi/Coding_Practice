class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return n
        i = last = 1
        while i<n:
            if nums[i]!=nums[i-1]:
                nums[last] = nums[i]
                last+=1
            i+=1
        return last
        
