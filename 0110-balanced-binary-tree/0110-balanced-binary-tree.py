# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(node,val=0):
            if not node:
                return True,val+1
            left = height(node.left,val)
            right = height(node.right,val)

            if (left[0] and right[0]) and abs(left[1]-right[1])<2:
                return True,max(left[1],right[1])+1
            return False,max(left[1],right[1])+1
        return height(root)[0]