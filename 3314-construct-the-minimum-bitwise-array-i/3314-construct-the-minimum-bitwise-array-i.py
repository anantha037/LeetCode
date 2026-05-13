class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        
        ans = []

        # check = 1


        for i in nums:
            check = i//2
            while check < i:
                if check | check +1 == i:
                    ans.append(check)
                    break
                check +=1
            else:
                ans.append(-1)

        return ans