class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # if len(time)==1:
        #     return time[0]
        l=1
        # if sum(time)<totalTrips:
        r = max(time)*totalTrips
        # else:
        #     r = sum(time)+1
        
        res = r
        while l<=r:
            mid = (r+l)//2
            curr = 0
            
            for t in time:
                curr+=mid//t
            print(l,mid,r,curr,res)
            # if curr==totalTrips:
            #     res = min(res,mid)
            #     r=mid-1
            if curr<totalTrips:
               
                l=mid+1
            else:
    
                res = min(res,mid)
                r=mid-1
        
        
     
        return res