# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        idx = {val:i for i,val in enumerate(inorder)}
        
        def helper(left, right):
            if left>right:
                return None
            val = postorder.pop()
            node = TreeNode(val)
            index = idx[val]
            
            node.right = helper(index+1, right)
            node.left = helper(left, index-1)
            
            return node
        return helper(0, len(inorder)-1)
