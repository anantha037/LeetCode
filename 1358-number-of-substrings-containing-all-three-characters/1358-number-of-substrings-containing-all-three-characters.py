class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        total = 0

        i=0
        j=1
        while i<=j and j<=len(s):
            if len(set(s[i:j]))<3:
                j+=1
            else:
                total += len(s)-j+1
                i+=1
        return total
            

            
