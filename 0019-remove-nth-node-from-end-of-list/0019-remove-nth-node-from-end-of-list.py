# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        second = head
        prev = None
        while n>0:
            second = second.next
            n-=1
        while second:
            prev = first
            first = first.next
            second = second.next
        if not prev:
            head=head.next
        elif first:
            prev.next = first.next
        else:
            prev.next = None
        return head

        
            


        