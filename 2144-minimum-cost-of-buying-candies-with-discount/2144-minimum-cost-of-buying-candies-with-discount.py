class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        if len(cost) == 1:
            return cost[0]
        cost.sort(reverse=True)

        res = 0
        
        for i in range(0,len(cost),3):
            res += cost[i]
            if i+1<len(cost):
                res += cost[i+1]
        return res