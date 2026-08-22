class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digit_sum = 0
        digit_product = 1

        for i in str(n):
            digit_sum+=int(i)
            digit_product*=int(i)
        return n%(digit_sum+digit_product)==0