class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        dict1={}
        for i in range(len(nums)-k+1):
            current=[]
            for j in nums[i:k+i]:
                if j in current:
                    continue
                dict1[j] = dict1.get(j,0)+1
                current.append(j)
        if min(dict1.values())!=1:
            return -1
        
        max_val = min(nums)
        for i in dict1:
            if dict1[i]==1:
                max_val = max(max_val,i)
        return max_val
    