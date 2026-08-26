class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        answers = []
        res = ''
        i,j=0,0
        obj = {'1':0,'0':0}
        while j<len(s):
            obj[s[j]]+=1
            # if obj['1']==k:
               
            if obj['1']>=k:
                while (obj['1']>k or s[i]=='0') and i<j:
                    obj[s[i]]-=1
                    i+=1
                if not res or len(res)>j-i+1:
                    res = s[i:j+1]
                    answers = [res]
                elif len(res)==j-i+1:
                    answers.append(s[i:j+1])
            j+=1
        # print(answers,res,obj,i,j)
        if not answers:
            return ''
        else:
            return sorted(answers)[0]