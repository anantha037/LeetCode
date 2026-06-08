class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        list1 = []
        list2 = []
        val = 0
        for i in nums:
            if i<pivot:
                list1.append(i)
            elif i>pivot:
                list2.append(i)
            else:
                val+=1
        return list1+[pivot]*val+list2