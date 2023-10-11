# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        
        # op = ''
        # if not root:
        #     return op
        # queue = deque([root,])
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node:
        #             op += str(node.val)+', '
        #             queue.append(node.left)
        #             queue.append(node.right)
        #         else:
        #             op += 'null, '
        # print(op)
        # return op
        def helperserialize(node, st):
            if not node: 
                st+='None,'
                return st
            st += str(node.val)+','
            st = helperserialize(node.left,st)
            st = helperserialize(node.right, st)
            
            return st
        return helperserialize(root,'')
    
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def rdeserialize(data):
            val = data[0]
            data.pop(0)
            if val =='None':
                return None
            node = TreeNode(val)
            node.left = rdeserialize(data)
            node.right = rdeserialize(data)
            return node
        datalist = data.split(',')
        root = rdeserialize(datalist)
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
