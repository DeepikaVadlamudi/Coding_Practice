class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        op = [0]*n
        left = 0 
        right = n-1
        for i in range(n-1, -1, -1):
            if abs(nums[left])>abs(nums[right]):
                square = nums[left]**2
                left+=1
            else:
                square = nums[right]**2
                right -=1
            op[i] = square
        return op
