class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        if len(set(nums)) == len(nums):
            return [0]*len(nums)
            
        obj = {}
        prefix = {}

        for i in range(len(nums)):
            if nums[i] in obj:
                obj[nums[i]].append(i)
                prefix[nums[i]].append(prefix[nums[i]][-1]+i)
            else:
                obj[nums[i]] = [i]
                prefix[nums[i]] = [i]

        res = [0]*len(nums)

        for i in obj:

            if len(obj[i])==1:
                res[obj[i][0]]=0
                continue
            for j in range(len(obj[i])):
                val = 0
                index = obj[i][j]

                before_values = j
                after_values = len(obj[i])-j-1

                after = prefix[i][-1] - prefix[i][j]
                before = prefix[i][max(0,j-1)]

                if before_values == 0:
                    before = 0
                elif after_values == 0:
                    after = 0

                left = abs((index*before_values)-before)
                right = abs((index*after_values)-after) 

                val = left+right
                
                res[obj[i][j]]=val

        return res
            
