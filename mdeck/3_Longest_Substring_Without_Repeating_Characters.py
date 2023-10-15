class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxlen = left = 0 
        n = len(s)
        for right in range(n):
            if s[right] in seen:
                left = max(left, seen[s[right]])
            maxlen = max(maxlen, right-left+1)
            seen[s[right]] = right+1
        return maxlen
