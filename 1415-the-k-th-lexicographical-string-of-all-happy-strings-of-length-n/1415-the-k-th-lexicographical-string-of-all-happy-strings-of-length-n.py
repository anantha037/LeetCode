class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        happy_strings = set()
        letters = 'abc'

        def backtrack(n,current):
            if len(happy_strings)==k:
                return
            if len(current)==n:
                happy_strings.add(current)
                return
            for i in range(max(n,3)):
                val = letters[i%3]
                if not current or current[-1] != val:

                    current+=val

                    backtrack(n,current)

                    current = current[:-1]
            
        
        backtrack(n,"")

        # if len(happy_strings)<k:
        #     return ""

        # print(len(happy_strings))
        happy_strings = sorted(happy_strings)
        # print(len(happy_strings),k,k-1,happy_strings[-1])
        
        return "" if k>len(happy_strings) else happy_strings[k-1]
        # return happy_string


            
            