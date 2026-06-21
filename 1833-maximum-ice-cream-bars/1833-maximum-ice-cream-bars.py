class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        def count_sort(arr):
            if not arr:
                return []
            n = len(arr)
            max_val = max(arr)
            cntArr = [0]*(max_val+1)
            for i in arr:
                cntArr[i] +=1

            for i in range(1,len(cntArr)):
                cntArr[i] += cntArr[i-1]

            ans = [0]*n

            for i in range(n-1,-1,-1):
                ans[cntArr[arr[i]]-1]=arr[i]
                cntArr[arr[i]]-=1

            return ans
        costs = count_sort(costs)
        total = 0

        for i in costs:
            coins-=i
            if coins<0:
                break
            total+=1
        return total