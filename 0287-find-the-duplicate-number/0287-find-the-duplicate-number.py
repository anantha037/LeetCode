class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        values = set()

        for i in nums:
            if i in values:
                return i
            values.add(i)
