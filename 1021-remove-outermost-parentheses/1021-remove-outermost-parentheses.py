class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        left_c=0
        right_c=0
        res = ''
        curr=''
        for i in s:
            if i=='(':
                left_c+=1
            else:
                right_c+=1
            curr+=i
            if left_c==right_c:
                res+=curr[1:-1]
                curr=''
        return res
