class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or t=="":
            return ""

        context, window = {},{}

        for c in t:
            context[c] = context.get(c, 0) +1

        matches, current = len(context), 0

        res, resLen = [-1,-1], float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]

            window[c] = window.get(c, 0) + 1

            if c in context and window[c] == context[c]:
                current += 1

            while current == matches:
                if resLen > (r-l+1):
                    res = [l,r]
                    resLen = (r-l+1)

                window[s[l]] -= 1

                if s[l] in context and window[s[l]] < context[s[l]]:
                    current -=1
                
                l+=1
        
        l,r = res

        return s[l:r+1] if resLen != float('inf') else ""


                




                        


            



