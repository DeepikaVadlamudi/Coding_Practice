# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0 
        stack = []
        stack.append((1,root))
        depth = 0 
        while stack:
            curdepth, node = stack.pop()
            if node:
                depth = max(depth,curdepth)
                stack.append((curdepth+1, node.left))
                stack.append((curdepth+1, node.right))
        return depth
