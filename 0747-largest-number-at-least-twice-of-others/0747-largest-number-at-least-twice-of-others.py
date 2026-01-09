class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxIndex=0
        m=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>m:
                m = nums[i]
                maxIndex=i
        
        for i in nums:
            if i!=m and i*2>m:
                return -1
        return maxIndex