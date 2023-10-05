class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        no_ind = 100000000 
        
        left = 0 
        right = 0 
        n = len(nums)
        sumt = 0
        for right in range(n):
            sumt+=nums[right]
            while sumt>=target:
                no_ind= min(no_ind, right-left+1)
                sumt -= nums[left]
                left+=1
        return 0 if no_ind == 100000000 else no_ind
