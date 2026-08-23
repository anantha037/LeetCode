# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node,curr=None):
            if not node:
                return curr==targetSum if curr else False
            if curr:
                curr+=node.val
            else:
                curr = node.val
            
            if not node.left and not node.right:
                if curr==targetSum:
                    return True
            
            if not node.left:
                right_sum = dfs(node.right,curr)
                return right_sum
        
            if not node.right:
                left_sum = dfs(node.left,curr)
                return left_sum

            left_sum = dfs(node.left,curr)
            right_sum = dfs(node.right,curr)

            return left_sum or right_sum
        return dfs(root)