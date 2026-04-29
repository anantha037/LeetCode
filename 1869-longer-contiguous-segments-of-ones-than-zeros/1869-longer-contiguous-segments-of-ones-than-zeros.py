class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        long_0=0
        long_1=0
        prev = s[0]
        count=1
        if prev=='0':
            long_0+=1
        else:
            long_1+=1
        for i in range(1,len(s)):
            if prev==s[i]:
                count+=1
            else:
                if prev=='1' and count>long_1:
                    long_1=count 
                elif prev=='0' and count>long_0:
                    long_0=count
                count=1
                prev=s[i]
        if count>0:
            if prev=='0' and count>long_0:
                long_0 = count
            elif prev=='1' and count+1>long_1:
                long_1 = count
        if long_1>long_0:
            return True
        return False