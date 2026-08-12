class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        i=1
        while i<len(nums):
            if nums[i]==nums[i-1]+1:
                prefix_sum+=nums[i]
            else:
                break
            i+=1
        
        nums = set(nums)
        while prefix_sum in nums:
            prefix_sum+=1
        return prefix_sum