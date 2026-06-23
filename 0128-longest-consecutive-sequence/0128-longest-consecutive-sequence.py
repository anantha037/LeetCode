class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(set(nums)) == 1:
            return 1
        
        maxLength = 1

        nums = set(nums)

        for i in nums:
            if i-1 not in nums:
                curr = 1
                val = i
                while val+1 in nums:
                    curr+=1
                    val+=1
                if curr > maxLength:
                    maxLength = curr
        
        return maxLength



    
        