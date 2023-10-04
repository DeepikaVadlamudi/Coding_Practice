class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sortheight = sorted(heights)
        count = 0 
        for i in range(len(heights)):
            if heights[i]!= sortheight[i]:
                count+=1
        return count
