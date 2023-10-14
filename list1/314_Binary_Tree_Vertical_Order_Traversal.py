# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#[[3],[9,8],[4,0,1,7]]-> [[4],[9],[3,0,1],[8],[7]]

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        traversal = defaultdict(list)
        queue = deque([(root,0)])
        minc = maxc = 0
        while queue:
            node, col = queue.popleft()
            if node:
                queue.append((node.left, col-1))
                queue.append((node.right, col+1))
                traversal[col].append(node.val)
                minc = min(minc, col)
                maxc = max(maxc,col)
        return [traversal[x] for x in range(minc,maxc+1)]
        
