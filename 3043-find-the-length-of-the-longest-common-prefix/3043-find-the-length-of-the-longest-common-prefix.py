class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        res = 0

        arr1 = set(arr1)
        arr2 = set(arr2)

        hash1 = set()
        hash2 = set()

        for num in arr1:
            hash1.add(num)
            val = str(num)
            prev = ''
            for i in range(len(val)):
                prev += val[i]
                hash1.add(int(prev))
        
        for num in arr2:
            hash2.add(num)
            val = str(num)
            prev = ''
            for i in range(len(val)):
                prev += val[i]
                hash2.add(int(prev))
                if int(prev) in hash1 and len(prev)>res:
                    res = len(prev)

        return res
        



