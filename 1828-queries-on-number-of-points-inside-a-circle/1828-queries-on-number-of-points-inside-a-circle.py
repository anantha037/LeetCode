class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        def euclidean_distance(point1,point2):
            val1 = (point2[0] - point1[0])**2
            val2 = (point2[1] - point1[1])**2
            return math.sqrt(val1+val2)
        res = []
        for query in queries:
            count = 0
            for point in points:
                if euclidean_distance(point,query[:2])<=query[2]:
                    count+=1
            res.append(count)
        return res