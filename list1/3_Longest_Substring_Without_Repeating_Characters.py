class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        left = right = i = count = 0
        seen = set()
        maxlen = 0
        while right<n:
            if s[right] in seen:
                while s[right] in seen:
                    seen.remove(s[left])
                    left+=1
            seen.add(s[right])
            maxlen = max(maxlen, right-left+1)
            right+=1

        return maxlen

        
