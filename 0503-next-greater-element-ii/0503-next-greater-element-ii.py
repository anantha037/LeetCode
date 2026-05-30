class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [-1]*n
        stack = []
        for i in range(n*2):
            index = i%n
            while stack and nums[index]>nums[stack[-1]]:
                answer[stack.pop()] = nums[index]
            
            stack.append(index)
        return answer