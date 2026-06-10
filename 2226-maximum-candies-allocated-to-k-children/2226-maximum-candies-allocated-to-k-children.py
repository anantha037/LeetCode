class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies)<k:
            return 0
        l = 1

        r = max(candies)

        res = 0

        while l<=r:
            mid = (l+r)//2
            curr=0

            for c in candies:
                curr += c//mid

            if curr<k:
                r = mid-1
            else:
                res = max(mid,res)
                l = mid+1
    
        return res