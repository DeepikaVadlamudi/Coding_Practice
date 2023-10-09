# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx = {val:i for i,val in enumerate(inorder)}
        self.preindex = 0
        def helper(left, right):
            if left>right:
                return None
            val = preorder[self.preindex]
            node = TreeNode(val)
            self.preindex += 1
            node.left = helper(left, idx[val]-1)
            node.right = helper(idx[val]+1, right)
            return node
        return helper(0, len(preorder)-1)
