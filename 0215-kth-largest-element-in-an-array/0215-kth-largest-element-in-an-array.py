class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        answers = []

        for i in nums:
            heapq.heappush(answers,i)
            if len(answers)>k:
                heapq.heappop(answers)

        return answers[0]
        