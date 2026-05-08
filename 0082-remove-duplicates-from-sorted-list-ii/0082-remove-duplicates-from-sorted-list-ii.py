# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        prev=dummy
        temp = head

        while temp:
            if temp.next and temp.val == temp.next.val:
                while temp.next and temp.val==temp.next.val:
                    temp=temp.next
                prev.next = temp.next
            else:
                prev = prev.next
            temp = temp.next
        return dummy.next
        
            
