# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root,):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def preorder(node,s):
            if not node:
                return ''
            s+=str(node.val)+','
            if node.left:
                s = preorder(node.left,s)
            else:
                s+='N,'
            if node.right:
                s = preorder(node.right,s)
            else:
                s+='N,'
            return s
        return preorder(root,'')

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        curr = data.split(',')

        i = 0
        def preorder(arr,i):
            if arr[i]=='N' or i>=len(arr):
                return None,i
            node = TreeNode(int(arr[i]))
            node.left,i = preorder(arr,i+1)
            node.right,i = preorder(arr,i+1)
            return node,i
        root,i = preorder(curr,i)
        return root
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# print(ser(Codec(root)))
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))