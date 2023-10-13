class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prodl = [1]*n
        prodr = [1]*n
        for i in range(1,n):
            prodl[i] = prodl[i-1]*nums[i-1]
        for i in range(n-2,-1,-1):
            prodr[i] = prodr[i+1]*nums[i+1]
        for i in range(n):
            nums[i] = prodl[i]*prodr[i]
        return nums
