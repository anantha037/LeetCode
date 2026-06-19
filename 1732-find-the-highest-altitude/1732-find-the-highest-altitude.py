class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        total =0
        for i in gain:
            total+=i
            if total>highest:
                highest=total
        return highest