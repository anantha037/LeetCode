"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        obj = {None:None}

        temp = head
        while temp:
            new_node = Node(temp.val)
            obj[temp] = new_node
            temp = temp.next
        temp = head
        while temp:
            curr = obj[temp]
            curr.next = obj[temp.next]
            curr.random = obj[temp.random]
            temp = temp.next
        return obj[head]



