class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n<2:
            return nums
        left = 0 
        right = n-1

        while left<=right:
            if nums[left]%2==0:
                left+=1
                continue
            if nums[right]%2!=0:
                right-=1
                continue
            if nums[left]%2==1 and nums[right]%2==0:
                nums[left], nums[right] = nums[right], nums[left]
                left+=1
                right-=1
        return nums
        
