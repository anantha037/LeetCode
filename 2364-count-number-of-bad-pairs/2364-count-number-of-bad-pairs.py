class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        count=0
        good_pairs ={}

        for i in range(len(nums)):
            diff = i-nums[i]

            good_count = good_pairs.get(diff,0)

            count+= i - good_count
        
            good_pairs[diff]=good_count+1
        
        return count