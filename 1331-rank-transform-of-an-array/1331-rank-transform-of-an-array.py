class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = sorted(set(arr))
        ht = {}
        val = 1
        for i in rank:
            ht[i]=val
            val+=1
        res = []

        for i in arr:
            res.append(ht[i])
        return res