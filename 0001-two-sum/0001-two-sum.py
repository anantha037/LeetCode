class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        obj = {}

        for i,x in enumerate(nums):
            check = target - x
            
            if check in obj:
                return [obj[check],i]
            obj[x]=i

        