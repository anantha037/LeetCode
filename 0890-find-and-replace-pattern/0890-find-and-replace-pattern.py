class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        count ={}
        for i in pattern:
            if i in count:
                continue
            else:
                count[i]=pattern.count(i)
        res=[]
        for i in words:
            current={}
            for j in i:
                if j in current:
                    continue
                else:
                    current[j]=i.count(j)
            for j,k in zip(count.values(),current.values()):
                if j!=k:
                    break
            else:
                
                for a,b in zip(count,current):
                    co_l = [x for x,y in enumerate(pattern) if y == a]
                    cu_l = [x for x,y in enumerate(i) if y == b]
                    print(co_l,cu_l)
                    if co_l !=cu_l:
                        break
                else:
                    res.append(i)
        return res