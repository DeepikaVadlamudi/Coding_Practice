class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        left = right = 0 
        n = len(s)
        count = 0  
        while right<n:
            if s[right] not in char:
                char[s[right]]=1
            else:
                char[s[right]]+=1
            while char[s[right]]>1:
                char[s[left]]-=1
                left+=1
            count = max(count,right-left+1)
            right+=1
        return count
