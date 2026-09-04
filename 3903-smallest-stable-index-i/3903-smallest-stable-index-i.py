class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        min_val = [nums[-1]]
        max_val = [nums[0]]
        n = len(nums)

        for i in range(n):
            max_val.append(max(nums[i],max_val[-1]))
            min_val.append(min(nums[n-i-1],min_val[-1]))
        min_val=min_val[::-1]
        for i in range(n):
            if max_val[i]-min_val[i]<=k:
                return i
        return -1