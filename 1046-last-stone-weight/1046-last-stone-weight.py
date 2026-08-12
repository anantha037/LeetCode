from queue import PriorityQueue
import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heapq.heapify_max(stones)
        
        curr = heapq.heappop_max(stones)
        
        while len(stones)>=1:
            print(stones,curr)
            second = heapq.heappop_max(stones)
            if curr == second:
                if not stones:
                    return 0
                curr = heapq.heappop_max(stones)
            else:
                curr -= second
                curr = heapq.heappushpop_max(stones,curr)

        return stones[-1] if stones else curr




        
        # if len(stones)<2:
        #     return stones[0]
        # queue = PriorityQueue()

        # for i in stones:
        #     queue.put(-i)
        # curr = -queue.get()

        # for i in range(0,len(stones)):
        #     print(curr)
        #     second = -queue.get()
        #     if curr==second:
        #         curr=0
        #     else:
        #         curr -= second
        #         queue.put(-curr)
        # return -queue.get()