class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        stack = []

        def backtrack(first,last):
            print(first,last,stack)
            if first==last==n:
                res.append("".join(stack))
                return
            if first<n:
                stack.append('(')
                first+=1
                backtrack(first,last)
                stack.pop()
                first-=1
            if last<first and stack:
                stack.append(')')
                last+=1
                backtrack(first,last)
                stack.pop()
                last-=1


        backtrack(0,0)
        print(res)
        return list(set(res))

