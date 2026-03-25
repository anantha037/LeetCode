class Solution:
    def maxSum(self, nums: List[int]) -> int:
        obj = {}

        for i in nums:
            val = max([int(j) for j in str(i)])
            if val in obj:
                obj[val].append(i)
            else:
                obj[val] = [i]
        
        pair_sums = []

        for i,j in obj.items():
            if not len(j)>1:
                continue
            j.sort()
            pair_sums.append(j[-1]+j[-2])
    
        if not pair_sums:
            return -1
        return max(pair_sums)
            

    