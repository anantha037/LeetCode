class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        if len(nums)<3:
            return len(nums)
        min_val = nums.index(min(nums))+1
        max_val = nums.index(max(nums))+1
        n = len(nums)

        if min_val<n-min_val+1:
            min_del = min_val
            min_opp = False
        else:
            min_del = n-min_val+1
            min_opp=True
        
        if max_val<n-max_val+1:
            max_del = max_val
            max_opp = False
        else:
            max_del = n-max_val+1
            max_opp = True
        
        if min_opp!=max_opp:
            if min_del<max_del:
                if max_opp:
                    res = min(min_del+max_del,max_val)
                else:

                    res = min(max_del+min_del,n-max_val+1)
            else:
                if max_opp:
                    res = min(min_del+max_del,n-min_val+1)
                else:
                    
                    res = min(max_del+min_del,min_val)
            return res
        else:
            return max(min_del,max_del)