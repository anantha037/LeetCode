import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        answers = []

        for i in range(len(points)):
            x1 = points[i][0]
            y1 = points[i][1]
            val = x1**2+y1**2
            heappush(answers, (val,points[i]))

        res = []
        for i in range(k):
            res.append(heappop(answers)[1])
        return res


        
        