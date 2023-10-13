class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        count = 0 
        for i in nums:
            if i-1 not in seen:
                curnum = i 
                curstreak =1
                while curnum+1 in seen:
                    curstreak +=1
                    curnum+=1
            count = max(count, curstreak)
        return count
