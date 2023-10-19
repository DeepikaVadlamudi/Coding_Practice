## Using memoization
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.maxval = {}
        def dp(i):
            if i==0:
                return nums[0]
            if i==1:
                return max(nums[0],nums[1])
            if i not in self.maxval:
                self.maxval[i] = max(dp(i-1), dp(i-2)+nums[i])
            return self.maxval[i]
        return dp(len(nums)-1)
