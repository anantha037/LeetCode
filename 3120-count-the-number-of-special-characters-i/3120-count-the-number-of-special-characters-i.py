class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0
        freq = Counter(word)

        for i in freq:
            if (i.isupper() and i.lower in freq) or (i.islower() and i.upper() in freq):
                count +=1
        return count