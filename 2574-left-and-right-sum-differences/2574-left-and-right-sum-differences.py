class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        res =[]
        for i in range(len(nums)):
            left_sum=sum(nums[:i])
            right_sum=sum(nums[i+1:])
            res.append(abs(left_sum-right_sum))
        return res