class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))

        while (w>1):
            if area%w==0:
                return [int(area//w),w]
            else:
                w-=1
        return [area, 1]

