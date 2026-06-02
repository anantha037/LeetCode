class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        freq = {}
        
        for day in responses:
            distinct = list(set(day))
            for response in distinct:
                freq[response] = freq.get(response,0)+1
        res = []
        max_val = max(freq.values())
        for i,j in freq.items():
            if j==max_val:
                res.append(i)
        if len(res)==1:
            return res[0]
        return sorted(res)[0]