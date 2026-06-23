class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        if len(nums)<=1:
            return 1
        nums = set(nums)
        visited = set()
        total = 0
        for i in nums:
            if i not in visited:
                curr = 1
                visited.add(i)
                temp = i+1
                while temp in nums:
                    temp+=1
                    visited.add(temp)
                    curr+=1
                total = max(total,curr)
        return total



    
        