class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        min_val = nums.index(min(nums))+1
        max_val = nums.index(max(nums))+1
        n = len(nums)

        if min_val>max_val:
            min_val,max_val = max_val,min_val
 
        front = max_val
        back = n-min_val+1
        both = min_val+(n-max_val+1)
        return min(front,back,both)

