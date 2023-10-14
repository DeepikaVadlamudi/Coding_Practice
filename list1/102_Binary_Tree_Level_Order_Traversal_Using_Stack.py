# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        if not root:
            return levels
        stack = [(root,0)]

        while stack:
            node, lev = stack.pop()
            if node:
                if len(levels)==lev:
                    levels.append([])
                levels[lev].append(node.val)
                stack.append((node.right, lev+1))
                stack.append((node.left, lev+1))
        return levels
        
