# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid(node, minimum = float('-inf'),maximum=float('inf')):
            if node.val <= minimum or node.val>=maximum:
                return False
            left_valid = isValid(node.left, minimum,node.val) if node.left else True
            right_valid = isValid(node.right,node.val,maximum) if node.right else True
            return left_valid and right_valid
        if not root:
            return True
        return isValid(root)