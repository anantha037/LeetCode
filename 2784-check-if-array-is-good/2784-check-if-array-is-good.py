class Solution:
    def isGood(self, nums: List[int]) -> bool:
        obj = Counter(nums)

        max_val = max(obj)
        
        if obj[max_val] != 2:
            return False
        elif len(nums) != max_val+1:
            return False
        else:
            for i in obj:
                if i != max_val and obj[i] != 1:
                    return False
        return True