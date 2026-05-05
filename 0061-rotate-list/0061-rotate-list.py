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
        
        last = temp
        k = k%n
        if k==n or k==0:
            return head
        
        count = 1
        temp = head

        while temp:
            if count == (n-k):
                break
            temp = temp.next
            count+=1
        
        first = temp.next
        temp.next = None
        last.next = head
        head = first

        return head

        
