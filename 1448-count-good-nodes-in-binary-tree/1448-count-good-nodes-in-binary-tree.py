# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,count=0,maximum=float('-inf')):
            if not node:
                return count
            if node.val>=maximum:
                count+=1
                maximum = node.val
            if node.left:
                count = dfs(node.left,count,maximum)
            if node.right:
                count = dfs(node.right,count,maximum)
            return count
        return dfs(root)