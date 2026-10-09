class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        answer=0
        i=0
        while i<len(s):
            if s[i]=='(':
                stack.append(s[i])
            else:
                if i+1<len(s) and s[i+1]==s[i]:
                    if stack:
                        stack.pop()
                    else:
                        print(stack,'hi')
                        answer+=1
                    i+=1
                else:
                    if stack:
                        stack.pop()
                        answer+=1
                    else:
                        answer+=2
            i+=1
        
        if stack:
            answer+= 2*len(stack)
        return answer