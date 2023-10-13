class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0 
        if x<0 or (x%10==0 and x!=0):
            return False
        while x>rev:
            val = x%10
            rev = rev*10 +val
            x = x//10
        return x==rev or x==rev//10
