class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)
        start, end = 0,n-1
        while start<=end:
            mid = start+(end-start)//2
            if letters[mid]<=target:
                start = mid+1
            else:
                end = mid-1
        if start == n:
            return letters[0]
        return letters[start]
