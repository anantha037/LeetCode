"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return
        
        visited = set()

        def clone(curr,visited,table={}):

            if not curr:
                return
            visited.add(curr)
            new_node = Node(curr.val)
            table[curr.val] = new_node
            for neighbor in curr.neighbors:
                if neighbor not in visited:
                    new_node.neighbors.append(clone(neighbor,visited,table))
                elif neighbor.val in table:
                    new_node.neighbors.append(table[neighbor.val])

            return new_node
        
        root = clone(node,visited)
        return root
        

