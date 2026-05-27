class Solution:
    def greatestLetter(self, s: str) -> str:
        res = ""
        
        if len(set(s))==1:
            return res
        
        checked = set()

        for c in s:
            if c.islower():
                if c.upper() in checked and res<c.upper():
                    res = c.upper()
                else:
                    checked.add(c)
            else:
                if c.lower() in checked and res<c:
                    res = c
                else:
                    checked.add(c)
        return res

