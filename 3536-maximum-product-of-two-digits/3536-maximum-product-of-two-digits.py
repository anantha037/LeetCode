class Solution:
    def maxProduct(self, n: int) -> int:
        val = [int(d) for d in str(n)]
        val.sort()
        return val[-1]*val[-2]