class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        n = len(nums)
        left = right = maxi = numzero = 0
        while right<n:
            if nums[right]==0:
                numzero+=1
                while numzero>1:
                    if nums[left]==0:
                        numzero-=1
                    left+=1  
            maxi = max(maxi, right-left+1)
            right+=1
        return maxi
