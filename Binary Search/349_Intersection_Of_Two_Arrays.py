class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen1 = set(nums1)
        seen2 = set(nums2)
        if len(seen1)<len(seen2):
            return [i for i in seen1 if i in seen2]
        else:
            return [i for i in seen2 if i in seen1]
