class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        obj = Counter(nums)
        count = obj[target]

        n = len(nums)
        max_len = min(count*2-1,n)
        if count<=1:
            return count
        total =0

        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    curr+=1
                if 2*curr>j-i+1:
                    total+=1
        return total

            
            




    
