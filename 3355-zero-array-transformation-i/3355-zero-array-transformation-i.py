class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0]*(len(nums)+1)
        
        for query in queries:
            start = query[0]
            end = query[1]
            diff[start] += 1
            diff[end+1] -=1
  
        for i in range(1,len(nums)+1):
            diff[i] += diff[i-1]
    
        for i in range(len(nums)):
            nums[i] -= diff[i]
        
        return True if max(set(nums)) <=0 else False