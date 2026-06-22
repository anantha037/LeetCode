class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        obj = Counter(text)

        total = 0
        for i in ['l','o']:
            if i in obj:
                obj[i]= obj[i]//2
            else:
                return 0
        for i in ['b','a','l','o','n']:
            if i in obj:
                curr = obj[i]
                if curr == 0:
                    return 0
                if total == 0:
                    total = curr
                else:
                    total = min(curr,total)
            else:
                return 0

        return total