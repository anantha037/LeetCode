class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        changes  = {}
        for i in nums:
            val = format(i,'032b')       
            for j in range(len(val)):
                if j not in changes:
                    changes[j] = [0,0]
                if val[j]=='0':
                    changes[j][0]+=1
                else:
                    changes[j][1]+=1
        
        total = 0
        for i in changes:
            total += changes[i][0]*changes[i][1]
        return total

                