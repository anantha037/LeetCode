class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        nums = []
        for i in range(left, right+1):
            digits = list(set(map(int, str(i))))
            for j in range(len(digits)):
                if digits[j]==0 or i%digits[j]!=0:
                    break
            else:
                nums.append(i)
        return nums
            