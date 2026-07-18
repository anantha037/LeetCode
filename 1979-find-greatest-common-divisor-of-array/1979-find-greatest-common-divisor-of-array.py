class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_n = min(nums)
        max_n = max(nums)

        return math.gcd(min_n,max_n)