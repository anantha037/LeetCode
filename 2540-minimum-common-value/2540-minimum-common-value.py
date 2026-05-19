class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1  = set(nums1)
        nums2 = set(nums2)
        
        for i in sorted(nums1):
            if i in nums2:
                return i
        return -1