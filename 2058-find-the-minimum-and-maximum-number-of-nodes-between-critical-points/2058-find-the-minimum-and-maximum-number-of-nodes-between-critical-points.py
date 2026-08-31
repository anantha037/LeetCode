# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        max_val = -1
        min_val = -1

        prev = head
        temp = head.next
        if not temp.next:
            return [min_val,max_val]

        values = []
        i=0
        while temp.next:
            if prev.val < temp.val > temp.next.val or prev.val > temp.val < temp.next.val:
                values.append(i)
            i+=1
            prev = temp
            temp = temp.next
        if not values or len(values)==1:
            return [min_val,max_val]
        max_val = values[-1]-values[0]
        min_val = float('inf')
        for i in range(1,len(values)):
            if values[i]-values[i-1]<min_val:
                min_val = values[i]-values[i-1]
        return [min_val,max_val]
        

        