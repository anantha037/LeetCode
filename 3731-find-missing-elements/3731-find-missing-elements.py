class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        min_val = nums[0]
        max_val = nums[-1]
        nums = set(nums)
        res =[]
        if len(nums) == max_val+1-min_val:
            return res
        else:
            for i in range(min_val, max_val+1):
                if i not in nums:
                    res.append(i)

            return res