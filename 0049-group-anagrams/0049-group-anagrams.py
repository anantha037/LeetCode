class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        obj = defaultdict(list)

        for s in strs:
            obj["".join(sorted(s))].append(s)
        
        return [i for i in obj.values()]