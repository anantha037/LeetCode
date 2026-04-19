class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        res = 0

        i = 0
        j = 0

        while i<=j:
            if i>=len(nums1) or j>=len(nums2):
                return res
            if nums1[i]>nums2[j]:
                i+=1
                if i>j:
                    j=i
            else:
                res = max(res,j-i)
                j+=1

        return res