class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            digits = [i for i in str(n)]
            product = 1
            for i in digits:
                product*=int(i)
            if product %t==0:
                return n
            n+=1
        