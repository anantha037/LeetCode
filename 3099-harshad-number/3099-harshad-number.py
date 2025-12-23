class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if len(str(x))==1:
            return x
        elif x % (int(str(x)[0])+int(str(x)[1]))==0:
            return int(str(x)[0])+int(str(x)[1])
        else:
            return -1