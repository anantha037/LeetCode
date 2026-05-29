class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')

        for n in nums:
            if n>9:
                curr = 0
                while n:
                    curr += n%10
                    n //= 10
                n = curr
                
            res = min(res,int(n))         
                
        return res