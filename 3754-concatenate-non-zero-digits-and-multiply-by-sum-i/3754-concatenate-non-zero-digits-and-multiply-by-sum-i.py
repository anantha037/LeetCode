class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = ''
        total = 0
        for i in str(n):
            if int(i)>0:
                x+=i
                total+=int(i)
        return int(x)*total if x else 0
        