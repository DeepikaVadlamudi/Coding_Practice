class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            print("less than 2")
            return x
        start = int(1)
        end = x//2
        while start<=end:
            mid = start + (end-start)//2
            num = mid*mid
            if num == x:
                return mid
            elif num < x:
                start = mid+1
            else:
                end = mid-1
        return end 
        
