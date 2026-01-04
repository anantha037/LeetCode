class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        rev = ''
        for i in range(k-1,-1,-1):
            rev+=s[i]

        return rev+s[k:]