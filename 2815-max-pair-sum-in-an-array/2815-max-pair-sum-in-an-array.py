class Solution:
    def maxSum(self, nums: List[int]) -> int:
        obj = {}
        for i in nums:
            val = [int(j) for j in str(i)]    
            max_val = max(val)
            if max_val in obj:
                obj[max_val].append(i)
            else:
                obj[max_val] = [i]
            
        pairs_sum = []
        for i in obj:
            if len(obj[i])>1:
                val = obj[i]
                val.sort()
                pairs_sum.append(val[-1]+val[-2])
        
        if not pairs_sum:
            return -1
        else:
            return max(pairs_sum)


        
            