class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        upper = [float('inf')]*26
        lower = [-1]*26

        for i in range(len(word)):
            if word[i].islower():
                val = ord(word[i])-97
                lower[val] = i
            else:
                val = ord(word[i])-65
                upper[val] = min(i, upper[val])
        
        count = 0

        for i in range(26):
            if lower[i] == -1 or upper[i] == float('inf'):
                continue
            elif upper[i]>lower[i]:
                count +=1
        return count
