# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def max_depth(node):
            left_height = max_depth(node.left) if node.left else 0
            right_height = max_depth(node.right) if node.right else 0
            return 1 + max(left_height,right_height)
        
        depth = max_depth(root)
        def dfs(node,height):
            if height == depth:
                return node.val
            height +=1
            left = dfs(node.left,height) if node.left else 0
            right = dfs(node.right,height) if node.right else 0
            return left+right

        total = dfs(root,1)
        return total

