class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res = []
        obj = set(dictionary)
        for i in range(len(queries)):
            word = queries[i]
            if word in obj:
                res.append(word)
                continue
            for j in range(len(dictionary)):
                check = dictionary[j]
                diff = 0
                for a,b in zip(word, check):
                    if diff>2:
                        break
                    if a!=b:
                        diff +=1
                if diff<=2:
                    res.append(word)
                    break
    
        return res