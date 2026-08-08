# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res =[root.val]
        def pathSum(node):
            if not node:
                return 0
            left_sum = pathSum(node.left)
            right_sum = pathSum(node.right)

            total = left_sum+right_sum+node.val
            res[0] = max(res[0],total,max(left_sum,right_sum,0)+node.val)
            return max(left_sum,right_sum,0)+node.val
            
        pathSum(root)
        return res[0]
