class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        obj = Counter(nums)

        heap = []

        for i in obj:
            heapq.heappush(heap,(-obj[i],i))
        
        res = []
        
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res