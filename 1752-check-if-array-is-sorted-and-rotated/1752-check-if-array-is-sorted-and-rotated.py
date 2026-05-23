class Solution:
    def check(self, nums: List[int]) -> bool:
        rotated = False

        for i in range(len(nums)-1):
            if nums[i]<=nums[i+1]:
                continue
            else:
                if rotated:
                    return False
                else:
                    rotated = True
                    if nums[-1]>nums[0]:
                        return False
        return True