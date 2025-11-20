class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = {}
        for i in range(len(groupSizes)):
            groups[groupSizes[i]] = groups.get(groupSizes[i],[])+[i]
        ans = []
        for i in groups:
            size = []
            for j in groups[i]:
                if len(size)==i:
                    ans.append(size)
                    size = []
                size.append(j)
            ans.append(size)
        return ans
            