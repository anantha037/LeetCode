class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,y1,x2,y2=0,1,2,3
        if rec1[x1]>rec2[x1]:
            rec1,rec2 = rec2,rec1
        if rec1[x2]<=rec2[x1]:
            print("1st")
            return False
        elif rec1[y2]<=rec2[y1] or rec1[y1]>=rec2[y2]:
            print("2nd")
            return False
        return True