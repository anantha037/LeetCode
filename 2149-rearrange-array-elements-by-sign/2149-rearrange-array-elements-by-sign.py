class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        j=1

        for i in range(0,len(nums),2):
            if nums[i]<0:
                while j<len(nums) and nums[j]<0:
                    j+=1
                if j<len(nums):
                    if j<i or i+1==j:
                        nums[i],nums[j]=nums[j],nums[i]
                    else:
                        val = nums[j]
                        for k in range(i,j):
                            nums[k] = nums[k+1]
                        nums[i]=val
                j+=1
        return nums
            