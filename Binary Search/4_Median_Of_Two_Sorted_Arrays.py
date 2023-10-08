class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        self.p1 = 0
        self.p2 = 0 

        def getmin():
            if self.p1<m and self.p2<n:
                if nums1[self.p1]<nums2[self.p2]:
                    ans = nums1[self.p1]
                    self.p1+=1
                else:
                    ans = nums2[self.p2]
                    self.p2+=1
            elif self.p2==n:
                ans = nums1[self.p1]
                self.p1+=1
            else:
                ans = nums2[self.p2]
                self.p2+=1
            return ans 
        
        if (m+n)%2 ==0:
            for _ in range((m+n)//2 - 1):
                answ = getmin()
            return (getmin()+getmin())/2
        else:
            for _ in range((m+n)//2):
                answ = getmin()
            return getmin()
                
        
