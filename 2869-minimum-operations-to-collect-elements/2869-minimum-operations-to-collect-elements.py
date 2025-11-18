class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        collection = [0]*k
        marked = 0

        for i in range(len(nums)-1,-1,-1):
            if marked==k:
                return len(nums)-i-1
            if nums[i]-1<k and collection[nums[i]-1]==0:
                collection[nums[i]-1] = 1
                marked+=1

        return len(nums)