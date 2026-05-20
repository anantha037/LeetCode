class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        freq = {}
        res = []
        count = 0
        for i in range(len(A)):
            freq[A[i]] = freq.get(A[i],0)+1
            freq[B[i]] = freq.get(B[i],0)+1

            if A[i] == B[i]:
                count+=1
            else:
                if freq[A[i]]==2:
                    count+=1
                if freq[B[i]]==2:
                    count+=1
            res.append(count)
        return res

