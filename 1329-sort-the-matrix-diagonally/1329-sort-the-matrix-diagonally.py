class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        
        diag = {}

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diff = i-j
                
                if diff in diag:
                    diag[diff].append(mat[i][j])
                else:
                    diag[diff] = [mat[i][j]]
        for diff in diag:
            diag[diff].sort()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                diff = i-j 
                mat[i][j] = diag[diff].pop(0)
        return mat