import numpy as np

class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        obj = {}
        res = []
        for word in dictionary:
            obj[word] = np.array(list(word))
        
        for word in queries:
            if word in obj:
                res.append(word)
            else:
                for arr in obj.values():
                    arr2 = np.array(list(word))
                    if np.sum(arr2 != arr) > 2:
                        continue
                    else:
                        res.append(word)
                        break

        return res