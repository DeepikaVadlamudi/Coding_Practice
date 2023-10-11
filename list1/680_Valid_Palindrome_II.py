class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(s,i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True
        start=0
        end = len(s)-1
        while start<=end:
            if s[start]!=s[end]:
                return check(s,start,end-1) or check(s,start+1,end)
            start+=1
            end-=1
        return True
            
