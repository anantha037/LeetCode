class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)

        def binary_search(nums,target,l,r):
            if l>=r:
                return -1
            mid = (r+l)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                return binary_search(nums,target,l,mid)
            else:
                return binary_search(nums,target,mid+1,r)
        
        return binary_search(nums,target,0,len(nums))


        