class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        count1 = Counter(s1)

        n = len(s1)
        i = 0

        while i<=len(s2)-n:
            if s2[i] in count1:
                word = s2[i:n+i]
                count2 = Counter(word)

                for j in range(n):
                    if word[j] not in count1:
                        i += j+1
                        break
                    else:
                        if count2[word[j]] > count1[word[j]]:
                            i += j+1
                            break
                else:
                    return True
            else:
                i+=1
        return False