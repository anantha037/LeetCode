class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        res = 0
        zeros=[]
        last=-1
        i=0
        while i<len(s):
            if s[i]=='1':
                res+=1
                i+=1
            else:
                last=i
                while i<len(s) and s[i]=='0':
                    i+=1
                zeros.append(s[last:i])

        if len(zeros)<2:
            return res
        elif len(zeros)==2:
            return len(s)
        else:
            delta = 0
            i=1
            while i<len(zeros):
                delta = max(delta, len(zeros[i-1])+len(zeros[i]))
                i+=1
            return delta+res
            
        