class Solution:
    def greatestLetter(self, s: str) -> str:
        s = set(s)
        if len(s)==1:
            return ''

        for i in range(90,64,-1):
            if chr(i) in s and chr(i+32) in s:
                return chr(i)

        return ''

