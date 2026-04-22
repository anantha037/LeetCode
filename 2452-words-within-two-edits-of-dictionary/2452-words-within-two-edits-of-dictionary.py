class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        obj = {}
        res = []
        for word in dictionary:
            obj[word] = list(word)
        
        for word in queries:
            if word in obj:
                res.append(word)
            else:
                for arr in obj.values():
                    arr2 = list(word)
                    if sum(el1 != el2 for el1, el2 in zip(arr, arr2)) > 2:
                        continue
                    else:
                        res.append(word)
                        break

        return res