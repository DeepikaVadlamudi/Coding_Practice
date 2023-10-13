class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=0:
            return 0
        if n==1:
            return 1 
        if n==2:
            return 2
        stairs = [0]*n
        stairs[0] =1
        stairs[1] =2
        i = 2
        while i<n:
            stairs[i] = stairs[i-1]+stairs[i-2]
            i+=1
        # print(stairs[-1])
        return stairs[-1]
