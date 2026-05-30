class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:

        stack = []
        n1 = len(nums1)
        n2 = len(nums2)
        next_greater = {}

        for i in range(n2):
            while stack and nums2[i]>stack[-1]:
                prev = stack.pop()
                next_greater[prev] = nums2[i]

            stack.append(nums2[i])
  
        answer = [-1]*n1

        for i in range(n1):
            if nums1[i] in next_greater:
                answer[i] = next_greater[nums1[i]]
        
        return answer