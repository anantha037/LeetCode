class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        l =[]
        for i in bank:
            if "1" in i:
                count=0
                for j in i:
                    if j=="1":
                        count+=1
                l.append(count)
        return sum(l[i]*l[i+1] for i in range(len(l)-1))