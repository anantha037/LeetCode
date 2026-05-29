class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for i in range(len(nums)):
            if len(str(nums[i]))>1:
                val = 0
                while nums[i]>0:
                    val+=nums[i]%10
                    nums[i]=nums[i]//10
                nums[i]=val
            
            if nums[i]<res:
                res = nums[i]
                
        return res