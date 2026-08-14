class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = {}
        res = 0
        curr = 0
        i =0
        j=0
        while j<len(s):
            val = s[j]
            count[val] = count.get(val,0)+1
            if count[val]>2:
                res = max(res,curr)
                while count[val]>2 and i<j:
                    count[s[i]]-=1
                    i+=1
                curr = j-i+1
            else:
                curr+=1
                res = max(res,curr)
            # print('i:',i,'j:',j,"curr:",curr,'res:',res,'count:',count)
            j+=1
        return res