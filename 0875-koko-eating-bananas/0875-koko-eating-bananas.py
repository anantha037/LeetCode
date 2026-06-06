class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h==len(piles):
            return max(piles)
        
        l = 1
        r = max(piles)

        res = r

        while l<=r:
            curr = 0
            mid = (l+r)//2
            for i in piles:
                curr += -(-i//mid)
            if curr<=h:
                res = min(res,mid)
                r=mid-1
            else:
                l=mid+1
        
        return res