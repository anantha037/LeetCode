class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        i=0
        j=0
        obj = dict()
        while j<len(nums):
            val = nums[j]
            obj[val] = obj.get(val,0)+1
            if obj[val]<=k:
                curr+=1
                res = max(res,curr)
            else:
                while obj[val]>k and i<j:
                    obj[nums[i]]-=1
                    curr=j-i
                    i+=1
            j+=1
        return res