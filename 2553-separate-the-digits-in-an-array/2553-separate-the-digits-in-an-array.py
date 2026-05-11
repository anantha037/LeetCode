class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for i in nums:
            if i>9:
                for j in str(i):
                    answer.append(int(j))
            else:
                answer.append(i)
        return answer