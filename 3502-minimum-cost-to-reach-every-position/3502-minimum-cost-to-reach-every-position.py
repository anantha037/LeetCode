class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        min_prefix = [cost[0]]

        for i in range(1,len(cost)):
            if min_prefix[i-1] > cost[i]:
                min_prefix.append(cost[i])
            else:
                min_prefix.append(min_prefix[i-1])
        
        return min_prefix
            