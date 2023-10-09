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
        
        queue = deque([root,])
        level = 0
        
        while queue:
            levels.append([])
            num_nodes = len(queue)
            for i in range(num_nodes):
                node = queue.popleft()
                levels[level].append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        return levels
