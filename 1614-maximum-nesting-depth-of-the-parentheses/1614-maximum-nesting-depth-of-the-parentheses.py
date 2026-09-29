class Solution:
    def maxDepth(self, s: str) -> int:
        total =[]
        current=0
        for i in s:
            if i=='(':
                current+=1
            elif i==")":
                current-=1
            total.append(current)

        return max(total)