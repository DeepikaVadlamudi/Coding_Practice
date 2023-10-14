class SparseVector:
    def __init__(self, nums: List[int]):
        self.list1 = {i:val for i,val in enumerate(nums) if val!=0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        prod = 0
        for i in self.list1:
            if i in vec.list1:
                prod += self.list1[i]*vec.list1[i]
        return prod

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
