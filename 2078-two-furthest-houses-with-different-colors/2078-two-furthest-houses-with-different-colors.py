class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0

        i,j = 0, len(colors)-1

        while i<j:
            if colors[i] != colors[j]:
                res = max(res,j-i,i)
            
            i+=1

        return res
