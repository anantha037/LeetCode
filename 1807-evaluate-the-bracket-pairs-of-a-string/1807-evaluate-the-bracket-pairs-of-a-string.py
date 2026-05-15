class Solution:
    def evaluate(self, s: str, knowledge: List[List[str]]) -> str:
        dict1={}
        new = s
        for i in knowledge:
            dict1[i[0]]=i[1]
        for i in range(len(s)):
            if s[i]=='(':
                starting =i+1
                continue
            if s[i]==')':
                if s[starting:i] in dict1:
                    new = new.replace('('+s[starting:i]+')',dict1[s[starting:i]])
                else:
                    new = new.replace('('+s[starting:i]+')','?')
        return new
            
            
            