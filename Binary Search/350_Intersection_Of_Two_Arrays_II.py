class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1)<len(nums2):
            count = Counter(nums1)
            for i in nums2:
                if i in count and count[i]>0:
                    res.append(i)
                    count[i] -=1
            return res
        else:
            count = Counter(nums2)
            for i in nums1:
                if i in count and count[i]>0:
                    res.append(i)
                    count[i] -=1
            return res
        
