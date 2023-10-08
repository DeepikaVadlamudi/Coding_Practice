class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1
        while start<end:
            mid = start+(end-start)//2
            if nums[mid]<nums[end]:
                end=mid
            elif nums[mid]>nums[end]:
                start = mid+1
            else:
                end -=1
            
        return nums[start]
                
        
