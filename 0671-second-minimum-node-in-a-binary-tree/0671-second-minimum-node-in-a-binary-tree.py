# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def find_min(curr,min_val=float('inf'),sec_min_val=float('inf')):
            if not curr:
                return sec_min_val

            if curr.val<min_val:
                sec_min_val = min_val
                min_val = curr.val
            elif min_val<curr.val<sec_min_val:
                sec_min_val = curr.val
            
            sec_min_val = find_min(curr.left,min_val,sec_min_val)
            sec_min_val = find_min(curr.right,min_val,sec_min_val)
            return sec_min_val
        
        if find_min(root) != float('inf'):
            return find_min(root)
        return -1
            
            
        