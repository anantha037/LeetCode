class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        q = []
        res = 0
        start = 0
        first = 0
        
        for i in range(len(nums)):
            if nums[i] == 1:
                res = max(res,i+1-first)
                continue
            else:
                k-=1
                q.append(i)
                res = max(res, i-first)
                if k<0:
                    k+=1
                    first = q.pop(0) + 1
        
        if k>=0:
            res = max(res,i+1-first)

        return res
