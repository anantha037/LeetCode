class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:

        answer = [0]*len(prices)
        mono_stack = []

        for i in range(len(prices)-1,-1,-1):
            while mono_stack and prices[i] < mono_stack[-1]:
                mono_stack.pop()

            if not mono_stack:
                answer[i] = prices[i]
            else:
                answer[i] = prices[i]-mono_stack[-1]
                
            mono_stack.append(prices[i])

        return answer