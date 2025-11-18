class Solution:
    def getLucky(self, s: str, k: int) -> int:
        num=''
        for i in range(len(s)):
            num+=str(ord(s[i])-96)
        for i in range(k):
            val = 0
            for i in num:
                val += int(i)
            num = str(val)
        return int(num)