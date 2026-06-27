class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_val = 1
        nums = set(nums)
        while min_val in nums:
            min_val+=1
        
        return min_val