# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], sum: int) -> bool:
        if root == None:
            return False
        stack = [(sum-root.val, root)]
        cursum = 0
        while stack:
            cursum, node = stack.pop()
            if not node.left and not node.right and cursum==0:
                return True
            if node.left:
                stack.append((cursum-node.left.val, node.left))
            if node.right:
                stack.append((cursum-node.right.val, node.right))
        return False
