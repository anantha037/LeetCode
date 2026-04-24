class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        obj = Counter(moves)
        
        return obj['_']+abs(obj['L']-obj['R'])
        