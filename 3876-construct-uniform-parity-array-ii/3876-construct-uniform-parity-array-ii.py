class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        even_count,odd_count = 0,0
        even_min,odd_min = float('inf'),float('inf')
        for i in nums1:
            if i%2==0:
                even_count+=1
                even_min = min(even_min,i)
            else:
                odd_count+=1
                odd_min = min(odd_min,i)

        if even_count==0 or odd_count==0:
            return True
        elif even_count==odd_count:
            return odd_min<even_min
        # elif even_count<odd_count:
        #     return even_min>odd_min
        else:
            return odd_min<even_min