class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = '123456789'
        res = []
        for i in range(len(digits)):
            for j in range(i+1,len(digits)):
                val = int(digits[i:j+1])
                if low<=val<=high:
                    res.append(val)
        res.sort()

        return res
            

            

