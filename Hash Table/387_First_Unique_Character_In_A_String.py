class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen={}
        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] =-1
            else:
                seen[s[i]] = i
        for i in seen:
            if seen[i] >=0:
                return seen[i]
        return -1
