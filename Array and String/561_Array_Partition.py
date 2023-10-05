class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sortednums = sorted(nums)
        sumt = 0 
        for i in range(0,len(sortednums),2):
            sumt+= sortednums[i]
        return sumt
