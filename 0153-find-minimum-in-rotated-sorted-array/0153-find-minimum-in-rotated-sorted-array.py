class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n==1:
            return nums[0]
        
        x = float('inf')

        l = 0
        r = len(nums)-1

        while l<=r:
            
            mid = l+(r-l)//2

            x = min(x, nums[mid])

            if nums[l]<=nums[mid]:
                if nums[l] > nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                r = mid-1
        
        return x
    




        
        return -1

