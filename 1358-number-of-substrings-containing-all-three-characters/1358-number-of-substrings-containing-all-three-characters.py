class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0
        l = 0
        count = {'a':0,'b':0,'c':0}
        n = len(s)
        for r in range(n):
            count[s[r]] +=1
            while count['a']>0 and count['b']>0 and count['c']>0:
                total += n-r
                count[s[l]]-=1
                l+=1
        return total
