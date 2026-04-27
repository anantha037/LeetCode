class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c=Counter(nums)
        sorted_c = dict(sorted(c.items(),reverse=True,key=lambda item:item[1]))
        n=[]
        for i in sorted_c:
            if k>0:
                n.append(i)
                k-=1
            else:
                break
        return n