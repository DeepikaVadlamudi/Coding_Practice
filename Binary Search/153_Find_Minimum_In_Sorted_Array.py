class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = 0, n-1
        while start<=end:
            mid = start+(end-start)//2
            if nums[mid]>nums[-1]:
                start=mid+1
            else:
                end = mid-1
        return nums[start]
