class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for i in range(rows):
            bottom = cols-1
            last = None
            while bottom>=0:
                if boxGrid[i][bottom] == '.':
                    if last:
                        j = last
                        last = None
                    else:
                        j = bottom-1
                    while j>=0 and boxGrid[i][j] == '.':
                        j-=1
                    if j>=0 and boxGrid[i][j] == '#':
                        boxGrid[i][j],boxGrid[i][bottom] = boxGrid[i][bottom],boxGrid[i][j]
                        last = j
                    elif j>=0 and boxGrid[i][j] =='*':
                        bottom = j

                bottom -=1
        
        rotated_box = [[None] * rows for _ in range(cols)]

        for row in range(rows):
            for col in range(cols):
                rotated_box[col][rows - row - 1] = boxGrid[row][col]
        
        return rotated_box 
    
        

