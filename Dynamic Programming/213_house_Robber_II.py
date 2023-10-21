class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=0:
            return 0 
        if n<=2:
            return max(nums[0],nums[1]) if n==2 else nums[0]
        
        def houserobber(arr):
            n = len(arr)
            if n<=2:
                return max(arr[0], arr[1]) if n==2 else arr[0]
            dp = [0]*n
            dp[0] = arr[0]
            dp[1] = max(arr[0],arr[1])
            for i in range(2,n):
                dp[i] = max(dp[i-1],dp[i-2]+arr[i])
            return dp[-1]

        
        return max(houserobber(nums[1:]), houserobber(nums[:n-1]))

        # print(first[-1],second[-1])     
