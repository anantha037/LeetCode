class Solution:
    def reverseDegree(self, s: str) -> int:
        index = 1
        base = 26
        total = 0
        for i in s:
            val = abs(ord(i)-97-base)
            total += val*index
            index+=1
        return total