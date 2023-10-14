# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        if not root:
            return levels
        queue = deque([root])
        res = []
        while queue:
            n = len(queue)
            cursum = 0
            for i in range(n):
                node = queue.popleft()
                if node:
                    cursum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            av = cursum/n
            res.append(av)

        return res          
