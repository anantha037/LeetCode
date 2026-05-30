class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []

        for i in range(len(prices)):
            j = i+1
            while j<len(prices) and prices[j]>prices[i]:
                j+=1
            if j<len(prices):
                answer.append(prices[i]-prices[j])
            else:
                answer.append(prices[i])
        
        return answer