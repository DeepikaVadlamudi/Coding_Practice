class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel = set(jewels)
        count = 0
        for i in stones:
            if i in jewel:
                count+=1
        return count
        
