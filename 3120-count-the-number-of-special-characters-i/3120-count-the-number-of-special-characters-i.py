class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        checked = set()
        for i in word:
            if i.islower() and i not in checked:
                checked.add(i)
                val = ord(i)-32
                if chr(val) in word:
                    count+=1
        return count