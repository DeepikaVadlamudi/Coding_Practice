class Solution:
    def binary_exp(self, x: float, n: int) ->float:
        if n ==0:
            return 1.0
        if n < 0:
            n = -1*n
            x = 1.0/x
        ans = 1
        while n!=0:
            if n%2 == 1:
                n = (n-1)
                ans *=x
            n = n/2
            x*=x
        return ans
    def myPow(self, x: float, n: int) -> float:
        ans = self.binary_exp(x,n)
        return ans
