class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)-1
        i = 0
        while i<n+1:
            if nums[i]==val:
                nums[i], nums[n] = nums[n], nums[i]
                n-=1
            else:
                i+=1
                
        return i
        
