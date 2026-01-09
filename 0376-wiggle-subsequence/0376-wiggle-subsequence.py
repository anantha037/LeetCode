class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        res=1
        prev = None

        for i in range(len(nums)-1):
            val = nums[i]-nums[i+1]
            if val>0 and prev!='pos':
                res+=1
                prev='pos'
            elif val<0 and prev!='neg':
                res+=1
                prev='neg'
        return res

                    
            
