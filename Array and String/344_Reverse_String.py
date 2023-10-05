class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0 
        j = n-1
        while i<=j:
            s[i], s[j] =s[j], s[i]
            i+=1
            j-=1
        print(s)
        
