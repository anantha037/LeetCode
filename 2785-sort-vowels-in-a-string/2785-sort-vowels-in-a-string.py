class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = {"a","A","e","E","i","I","o","O","u","U"}

        current = []

        for l in s:
            if l in vowels:
                current.append(l)
        
        current.sort()

        count = 0

        t = ""
        
        for l in s:
            if l in vowels:
                t += current[count]
                count+=1
            else:
                t+=l
        return t