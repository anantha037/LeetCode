class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        count = 0

        checked = {}

        for i in range(len(word)):
            if word[i].islower():
                c = word[i]
                if c in checked:
                    checked[c] = [i, checked[c][1]]
                else:
                    checked[c] = [i,float('inf')]
            else:
                c = word[i].lower()
                if c in checked:
                    checked[c] = [checked[c][0],min(i, checked[c][1])]
                else:
                    checked[c] = [-1,i]
        
        count = 0

        for c in checked:
            val = checked[c]
            if val[0] == -1 or val[1] == float('inf'):
                continue
            elif val[0] < val[1]:
                count +=1
        return count
