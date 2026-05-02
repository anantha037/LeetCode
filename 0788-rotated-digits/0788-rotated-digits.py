class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid = set([3,4,7])
        self_rotate = set([0,1,8])

        total = 0
        for i in range(1,n+1):
            curr = set([int(j) for j in str(i)])
            for j in invalid:
                if j in curr:
                    break
            else:
                if curr <= self_rotate:
                    continue
                total +=1
                

        return total

