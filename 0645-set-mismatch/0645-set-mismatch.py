class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        obj ={}

        extra = False
        missing = False

        for i in range(1, len(nums)+1):
            if nums.count(i)==0:
                missing = i
            elif nums.count(i)==2:
                extra = i

            if extra and missing:
                return [extra, missing]

        return [extra, missing]