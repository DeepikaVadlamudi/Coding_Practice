class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = last = 1
        n = len(nums)
        while i<n:
            if nums[i]==nums[i-1]:
                i+=1
            else:
                nums[last]= nums[i]
                last+=1
                i+=1
        return last
