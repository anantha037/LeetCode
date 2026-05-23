class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        words = s.split(" ")
        last = float('-inf')

        def isnum(val):
            try:
                float(val)
                return True
            except:
                return False

        for word in words:
            if isnum(word):
                if float(word)>last:
                    last=float(word)
                else:
                    return False
        
        return True