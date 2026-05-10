class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        n = len(s1)
        freq1 = [0] * 26
        freq2 = [0] * 26

        for i in range(n):
            freq1[ord(s1[i])-97] += 1
            freq2[ord(s2[i])-97] += 1
        
        if freq1 == freq2:
            return True
        for i in range(n,len(s2)):
            freq2[ord(s2[i-n])-97] -=1
            freq2[ord(s2[i]) - 97] +=1

            if freq1 == freq2:
                return True
            
        return False
        