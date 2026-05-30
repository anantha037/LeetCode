class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        obj = Counter(nums)

        def backtrack(curr):
            if len(curr) == len(nums):
                result.append(curr[:])
    
                return
    
            for i in obj:
                if obj[i]==0:
                    continue
                curr.append(i)
                obj[i]-=1
                backtrack(curr)
            
                curr.pop()
                obj[i]+=1
        
        backtrack([])
        return result