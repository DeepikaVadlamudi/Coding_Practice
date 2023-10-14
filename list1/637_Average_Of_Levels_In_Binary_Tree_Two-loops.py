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
        level = 0 
        while queue:
            n = len(queue)
            levels.append([])
            for i in range(n):
                node = queue.popleft()
                if node:
                    levels[level].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level+=1
        res = [0]*len(levels)
        for i in range(len(levels)):
            cursum = 0
            n = len(levels[i])
            for j in range(n):
                cursum+=levels[i][j]
            av = cursum/n
            res[i]=av 

        return res          
