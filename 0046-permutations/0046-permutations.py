class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(num,remaining):
            if len(num)==len(nums):
                answer.append(num)
                return
            
            for i in range(len(remaining)):
                backtrack(num+[remaining[i]],remaining[:i]+remaining[i+1:])

        backtrack([],nums)
        return answer