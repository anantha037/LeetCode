class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        checked = set()
        for edge in edges:
            if edge[0] in checked:
                return edge[0]
            else:
                checked.add(edge[0])
            
            if edge[1] in checked:
                return edge[1]
            else:
                checked.add(edge[1])