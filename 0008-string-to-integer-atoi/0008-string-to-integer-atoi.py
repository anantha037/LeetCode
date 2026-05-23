class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if len(s)==0:
            return 0
        res = ""

        if s[0] == '-':
            start = 1
            negative = True
        elif s[0] == '+':
            start = 1
            negative = False
        else:
            negative = False
            start = 0
        exceptions = '+ -.'
        for i in range(start,len(s)):
            if s[i].isalpha() or s[i] in exceptions:
                break
            else:
                res += s[i]
        
        if not res:
            return 0
        else:
            if negative:
                res = max(-2**31,-int(res))
            else:
                res = min(2**31-1,int(res))
            
            return res