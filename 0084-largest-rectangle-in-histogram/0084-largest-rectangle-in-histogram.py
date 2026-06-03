class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        stack = []

        i = 0
        
        while i<len(heights):
            index = i
            while stack and stack[-1][1]>=heights[i]:
                popped = stack.pop()
                area = max(popped[1]*(i-popped[0]),area)
                index = popped[0]
            stack.append([index,heights[i]])
            i+=1
        
        while stack:
            area = max((len(heights)-stack[-1][0])*stack[-1][1],area)
            stack.pop()
        return area
            