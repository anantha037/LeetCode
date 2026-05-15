class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dict1={}
        for i in cpdomains:
            current = i.split(" ")
            times = int(current[0])
            domain = current[1].split(".")
            domain.reverse()
            for j in range(len(domain)):
                curr = domain[:j+1]
                curr.reverse()
                dom = ".".join(curr)
                dict1[dom] = dict1.get(dom,0)+times
        res=[]
        for i,j in dict1.items():
            current = str(j)+" "+str(i)
            res.append(current)
        return res            