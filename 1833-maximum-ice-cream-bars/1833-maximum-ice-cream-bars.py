class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        total = 0

        for i in costs:
            coins-=i
            if coins<0:
                break
            total+=1
        return total