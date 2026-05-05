# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        temp = head
        n = 1

        while temp.next:
            temp = temp.next
            n += 1
        
        if k==n:
            return head
        elif k>n:
            target = n - (k%n)
        else:
            target = n-k

        temp = head
        count = 1

        while count < target:
            temp = temp.next
            count +=1
        
        if not temp or not temp.next:
            return head
        
        first = temp.next

        while first.next:
            first = first.next
 
        first.next = head
        head = temp.next
        temp.next = None

        
        return head
