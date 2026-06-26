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
        obj = {}
        if not head:
            return None
        temp = head
        while temp:
            new_node = Node(temp.val)
            new_node.next = temp.next
            temp.next = new_node
            temp = new_node.next
        n = 0

        temp = head
        while temp and temp.next:
            obj[n] = temp.random.next if temp.random else None
            n+=1
            temp = temp.next.next
        
        head = head.next
        temp = head
        n = 0
        while temp:
            temp.random = obj[n]
            n+=1
            if not temp.next:
                break
            temp.next = temp.next.next
            temp = temp.next

        return head



