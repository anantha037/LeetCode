class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val = float('inf')
        max_val = float('-inf')
        for i in nums:
            if i<min_val:
                min_val=i
            if i>max_val:
                max_val=i
        
        res = []
        if len(nums) == max_val+1-min_val:
            return res
        else:
            for i in range(min_val, max_val+1):
                if i not in set(nums):
                    res.append(i)

            return res