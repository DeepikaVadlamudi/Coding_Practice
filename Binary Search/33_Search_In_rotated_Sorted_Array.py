class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        start = 0
        end = n-1
        while start<=end:
            mid = start + (end-start)//2
            if nums[mid]<=nums[-1]:
                end = mid-1
            else:
                start = mid+1
        k = n - start
        left, right = 0, n-1
        while left<=right:
            mid = left + (right-left)//2
            act_mid = (mid-k)%n
            if nums[act_mid]==target:
                return act_mid
            elif nums[act_mid]<target:
                left = mid+1
            else:
                right = mid-1
        return -1
