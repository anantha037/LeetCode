# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def identical(p,q):
            if not p and not q:
                return True
            elif not p or not q or p.val!=q.val:
                return False
            return identical(p.left,q.left) and identical(p.right,q.right)
        # exist = False
        if not root:
            return False
        
        if root.val == subRoot.val:
            if identical(root,subRoot):
                return True

        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
