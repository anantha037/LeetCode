class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0

        i,j = 0, len(colors)-1

        while i<j:
            if colors[i] != colors[j]:
                res = max(res,j-i,i)
            
            i+=1

        return res




        # diff = 0
        # for i in range(len(colors)):
        #     for j in range(i+1,len(colors)):
        #         if colors[i]!=colors[j] and diff<abs(i-j):
        #             diff=abs(i-j)
        # return diff