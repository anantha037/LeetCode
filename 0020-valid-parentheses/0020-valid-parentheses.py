class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
            '(':')',
            '[':']',
            '{':'}',
        }

        stack = []

        for char in s:
            if char in pairs:
                stack.append(pairs[char])
            else:
                if stack and stack[-1] == char:
                    stack.pop()
                else:
                    return False
        
        return True if not stack else False