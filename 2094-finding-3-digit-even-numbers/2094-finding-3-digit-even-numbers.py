class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        res = []
        
        for i in range(100,999,2):
            curr = [int(j) for j in str(i)]
            check = Counter(curr)

            if all(count[j] >= check[j] for j in curr):
                res.append(i)
        return res
