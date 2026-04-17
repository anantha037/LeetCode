class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = 0

        pos = {}

        last = -1

        for i in range(len(s)):
            if s[i] not in pos:
                pos[s[i]] = i

            else:
                last = max(last,pos[s[i]])
                pos[s[i]] = i
            res = max(res,i-last)

        return max(res,i-last)




            