# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node,target,ancestors):
            ancestors.append(node)
            if node==target:
                return ancestors
            if node.val<target.val:
                return dfs(node.right,target,ancestors)
            else:
                return dfs(node.left,target,ancestors)
        
        first = dfs(root,p,[])
        second = dfs(root,q,[])

        if len(first)>len(second):
            first,second = second,first

        second = set(second)

        for i in range(len(first)-1,-1,-1):
            if first[i] in second:
                return first[i]
            

            
            

            

        