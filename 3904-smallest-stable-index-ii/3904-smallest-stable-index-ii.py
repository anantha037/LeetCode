class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        max_val = [nums[0]]
        min_val = [nums[-1]]
        n=len(nums)
        for i in range(1,n):
            max_val.append(max(max_val[-1],nums[i]))
            min_val.append(min(min_val[-1],nums[n-i-1]))
        
        min_val=min_val[::-1]
        
        for i in range(n):
            if max_val[i]-min_val[i]<=k:
                return i
        return -1