class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        words = {}

        for i in range(len(s)):
            word = s[i]
            if word in words:
                words[word][i] = 1
            else:
                words[word] = [0]*len(s)
                words[word][i] = 1

        res = 0

        temp = k
            
        for word in words:

            q = []
            start = 0
            first = 0
            
            for i in range(len(words[word])):
                if words[word][i] == 1:
                    res = max(res,i+1-first)
                    continue
                else:
                    k-=1
                    q.append(i)
                    res = max(res, i-first)
                    if k<0:
                        k+=1
                        first = q.pop(0) + 1
            
            if k>=0:
                res = max(res,i+1-first)

            k = temp
        return res