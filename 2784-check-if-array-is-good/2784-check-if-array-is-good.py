class Solution:
    def isGood(self, nums: List[int]) -> bool:
        
        freq = {}
        
        max_val = float('-inf')

        times = 0

        for num in nums:
            if num>max_val:
                max_val = num
            freq[num] = freq.get(num,0) + 1
            if freq[num] == 2:
                times +=1
            if times>1:
                return False

        if freq[max_val] != 2 or len(nums) != max_val+1:
            return False

        return True