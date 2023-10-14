class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l = len(nums1)
        m= m-1
        n = n-1
        for i in range(l-1,-1,-1):
            if n<0:
                break
            if nums1[m]>nums2[n] and m>=0:
                nums1[i] = nums1[m]
                m-=1
            else:
                nums1[i] =nums2[n]
                n-=1
                
