class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [nums[0]]
        suffix = [nums[-1]]
        res = []
        for i in range(1,len(nums)-1):
            prefix.append(prefix[i-1]*nums[i])
            suffix.append(suffix[i-1]*nums[len(nums)-i-1])
    
        # for i in range(len(nums)):
        res = [suffix[-1]]

        for i in range(len(nums)-2):
            res.append(prefix[i]*suffix[len(nums)-i-3])

        res.append(prefix[-1])
        
        return res
        # for i in range(len(nums)):
        # res = [suffix[-1]]

        # for i in range(len(nums)-2):
        #     res.append(prefix[i]*suffix[len(nums)-i-3])

        # res.append(prefix[-1])
        
        # return res
        