class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        res = ""
        for word in words:
            total = 0
            for ch in word:
                total += weights[ord(ch)-97]
            total %= 26
            res += chr(122-total)

        return res
