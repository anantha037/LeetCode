class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            row = list(filter(lambda x: x != '.',i))
            if len(row) != len(set(row)):
                return False
        
        for i in range(len(board)):
            col = []
            for j in range(len(board)):
                if board[j][i] != '.':
                    col.append(board[j][i])
            if len(col) != len(set(col)):
                return False
                
        grids = {}

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] =='.':
                    continue
                indexes = (i//3, j//3)

                if indexes not in grids:
                    grids[indexes] = set(board[i][j])
                else:
                    if board[i][j] in grids[indexes]:
                        return False
                    else:
                        grids[indexes].add(board[i][j])

        return True