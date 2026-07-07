# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def inorder(root,value=0):
            if not root:
                return value
            value = inorder(root.right,value)
            value+=root.val
            root.val = value
            value = inorder(root.left,value)

            return value
        inorder(root)
        return root
