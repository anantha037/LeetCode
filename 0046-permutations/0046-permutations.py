class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def backtrack(num):
            if len(num)==len(nums):
                answer.append(num)
                return
            
            for i in nums:
                if num and i in set(num):
                    continue
                backtrack(num+[i])

        backtrack([])
        return answer