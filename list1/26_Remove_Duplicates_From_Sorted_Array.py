class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n<2:
            return True
        last = 0 
        i = 1 
        while i<n:
            if nums[i]!=nums[i-1]:
                last+=1
                nums[last] = nums[i]
            i+=1

        return last+1
