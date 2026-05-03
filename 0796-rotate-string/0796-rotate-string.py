class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        
        for i in range(len(s)):
            if s[i] == goal[0] and s[i:]+s[:i] == goal:
                return True
        
        return False