class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        answer = ""

        n1 = len(t)
        n2 = len(s)

        freq1 ={}
        freq2 = {}

        for char in t:
            freq1[char] = freq1.get(char,0) + 1
            freq2[char] = 0

        matches = 0

        l = 0
        r = 0

        while l<n2 and r<n2:
            char = s[r]
            
            if char in freq1:
                freq2[char] +=1
                if freq2[char] <= freq1[char]:
                    matches += 1
            else:
                freq2[char] = freq2.get(char,0) + 1
            # print(l,r,char,matches)
            while matches == n1 and l<=r:

                current = len(s[l:r+1])

                if not answer:
                    
                    answer = s[l:r+1]
                elif current<len(answer):
                    answer = s[l:r+1]

                freq2[s[l]] -= 1
                if s[l] in freq1:
                    if freq2[s[l]] < freq1[s[l]]:
                        matches -= 1
                    
                l +=1
            
            r+=1
        
        return answer


                




                        


            



