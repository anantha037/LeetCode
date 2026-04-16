class Solution:
    def trap(self, height: List[int]) -> int:
        i,j = 0, len(height)-1
        left_max = -1
        right_max = -1

        res = 0

        while i<j:
            if height[i]<=height[j]:
                if left_max-height[i]>0:
                    res += left_max-height[i]
                left_max = max(left_max,height[i])
                i += 1
            else:
                if right_max - height[j] > 0:
                    res += right_max - height[j]
                right_max = max(right_max,height[j])
                j -=1
        return res



