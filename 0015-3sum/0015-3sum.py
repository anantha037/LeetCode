class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        nums.sort()
        checked = set()
        for i in range(len(nums)-1):
            if nums[i] in checked:
                continue
            j = i+1
            k = len(nums)-1
            target = -nums[i]
            current = set()
            while j<k:
                if nums[j] in current:
                    j+=1
                    continue
                if nums[k] in current:
                    k-=1
                    continue
                if nums[j]+nums[k]==target:
                    res.append([nums[i],nums[j],nums[k]])
                    current.add(nums[j])
                    current.add(nums[k])
                    j+=1
                    k-=1
                elif nums[j]+nums[k] <target:
                    j+=1
                else:
                    k-=1
                
            checked.add(nums[i])
        return res
