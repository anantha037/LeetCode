class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        diff_values = list(set(arr1)-set(arr2))
        arr1_values = Counter(arr1)

        res = []

        for i in range(len(arr2)):
            val = arr2[i]
            res.extend([val]*arr1_values[val])
        
        diff_values.sort()

        for i in range(len(diff_values)):
            val = diff_values[i]
            res.extend([val]*arr1_values[val])

        return res

                    

        

