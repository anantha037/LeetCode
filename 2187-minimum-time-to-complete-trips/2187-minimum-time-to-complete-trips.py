class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # if len(time)==1:
        #     return time[0]
        l=1
        r = max(time)*totalTrips
        
        res = r
        while l<=r:
            mid = (r+l)//2
            curr = 0
            
            for t in time:
                curr+=mid//t
                if curr>=totalTrips:
                    break
           
            if curr<totalTrips:
                l=mid+1
            else:
                res = min(res,mid)
                r=mid-1

        return res