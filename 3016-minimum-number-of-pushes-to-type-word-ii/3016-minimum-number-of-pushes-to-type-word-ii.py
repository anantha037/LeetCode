class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = Counter(word)
        
        sorted_freq = dict(sorted(freq.items(), key=lambda x: x[1], reverse=True))

        count = 0
        res = 0
        for i in sorted_freq:
            res += sorted_freq[i]*((count//8)+1)
            count+=1
            
        return res
