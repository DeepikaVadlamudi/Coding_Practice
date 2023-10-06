class Solution:
    def isHappy(self, n: int) -> bool:
        def getnext(num):
            sumt = 0 
            while num>0:
                dig = num%10
                num = num//10
                sumt+=dig**2
            return sumt
        
        slow = n
        fast = getnext(n)
        while fast!=1 and slow!=fast:
            slow = getnext(slow)
            fast = getnext(getnext(fast))
        return fast ==1
