# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=0
        res = []
        temp = head
        while temp:
            n+=1
            temp =temp.next
        temp = head
        for i in range(n%k):
            curr=temp
            for j in range((n//k)):
                if temp: 
                    temp = temp.next
            last = temp
            if temp:
                temp = temp.next
            if last:
                last.next = None
            res.append(curr)
        for i in range(n%k,k):
            curr = temp
            for j in range((n//k)-1):
                if temp: 
                    temp = temp.next
            last = temp
            if temp:
                temp = temp.next
            if last:
                last.next = None
            res.append(curr)
        return res
        