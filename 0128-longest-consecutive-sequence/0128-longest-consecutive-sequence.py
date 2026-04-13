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
            


        # for i in nums:
        #     obj[i] = obj.get(i,1)
        #     if i+1 in nums:
        #         obj[i+1] = obj.get(i+1, 1) + obj[i]
        #         obj[i] += 1
        #     if i-1 in nums:
        #         obj[i-1] = obj.get(i-1,1) + 1
        #         obj[i] = obj[i-1] + 1
        
        # if max(obj.values())==1:
        #     return 1
        # else:
        #     return max(obj.values()) // 2


        