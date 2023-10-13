class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero = 0
        count = 0
        for i in range(len(nums)):
            if nums[i]!=0:
                product *= nums[i]
                count+=1
            else:
                zero+=1
        if count == 0:
            product = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if zero>=1:
                    nums[i] = 0
                else:
                    nums[i] = product//nums[i]
            else:
                if zero>1:
                    nums[i] = 0
                else:
                    nums[i] = product
        return nums
