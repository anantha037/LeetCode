class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(curr, remaining):
            if len(curr) == len(nums) and curr not in result:
                result.append(curr)
                return
            
            for i in range(len(remaining)):
                backtrack(curr+[remaining[i]],remaining[:i]+remaining[i+1:])
            
        
        backtrack([], nums)
        return result