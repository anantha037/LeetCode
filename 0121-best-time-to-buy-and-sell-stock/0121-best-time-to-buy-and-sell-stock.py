class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0

        left_min = float('inf')
        curr_max = -1
        for i in range(0,len(prices)):
            if left_min>prices[i]:
                left_min = prices[i]
                
                curr_max = -1
            elif prices[i]>curr_max:
                curr_max = prices[i]

            profit = max(profit,curr_max-left_min)

        return profit
        
