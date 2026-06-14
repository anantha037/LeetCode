# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        total = 0
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow
        temp = second
        prev = None
        while temp:
            next_node = temp.next
            temp.next = prev
            prev = temp
            temp = next_node
        
        first = prev
        second = head
        while first:
            val = first.val+second.val
            if val>total:
                total = val
            first = first.next
            second = second.next
        return total