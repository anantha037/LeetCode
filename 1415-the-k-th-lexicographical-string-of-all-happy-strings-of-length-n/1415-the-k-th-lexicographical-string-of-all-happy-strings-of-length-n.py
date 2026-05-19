class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        happy_strings = set()

        def backtrack(n,current):
            if len(happy_strings)>=k:
                return
            if len(current)==n:
                happy_strings.add(current)
                return
            for i in 'abc':
                if not current or current[-1] != i:

                    current+=i

                    backtrack(n,current)

                    current = current[:-1]
            
        
        backtrack(n,"")

        happy_strings = sorted(happy_strings)
        
        return "" if k>len(happy_strings) else happy_strings[k-1]


            
            