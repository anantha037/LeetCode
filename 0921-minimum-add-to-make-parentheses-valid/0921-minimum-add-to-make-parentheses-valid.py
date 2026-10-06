class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        c_count = 0

        for i in s:
            if i=='(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                else:
                    c_count+=1
        
        return len(stack)+c_count