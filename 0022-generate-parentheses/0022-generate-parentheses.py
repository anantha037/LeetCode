class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtrack(first,last,s):
            if first==last==n:
                res.append(s)
                return
            if first<n:
                backtrack(first+1,last,s+'(')

            if last<first:
                backtrack(first,last+1,s+')')
        


        backtrack(0,0,'')
        print(res)
        return list(set(res))

