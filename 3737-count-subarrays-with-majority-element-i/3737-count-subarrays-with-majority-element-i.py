class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        obj = Counter(nums)
        count = obj[target]

        n = len(nums)
        min_len = 1
        max_len = min(count*2-1,n)
        if max_len<0:
            return 0
        elif max_len==1:
            return count
        # elif max_len==n:
        #     print('HI')
        #     return n*(n+1)//2
        
        total =0

        for i in range(len(nums)):
            curr = 0
            for j in range(i,len(nums)):
                if nums[j]==target:
                    curr+=1
                if 2*curr>j-i+1:
                    total+=1
                    # print(i,j,total)
            # print(i,curr,total)
        return total

            
            




    
