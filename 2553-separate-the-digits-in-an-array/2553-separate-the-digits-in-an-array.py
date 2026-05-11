class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []

        for i in nums:
            answer.extend(int(j) for j in str(i))
        return answer