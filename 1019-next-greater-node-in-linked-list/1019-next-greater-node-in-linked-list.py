# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        stack = []
        answer=[]
        temp = head
        index = defaultdict(list)
        i=0
        while temp:
            if not stack or stack[-1]>=temp.val:
                stack.append(temp.val)
            else:
                while len(stack)>0 and stack[-1]<temp.val:
                    curr = stack.pop()
                    curr_i = index[curr].pop()
                    answer[curr_i] = temp.val
                stack.append(temp.val)
            index[temp.val].append(i)
            temp = temp.next
            i+=1
            answer.append(0)
        return answer