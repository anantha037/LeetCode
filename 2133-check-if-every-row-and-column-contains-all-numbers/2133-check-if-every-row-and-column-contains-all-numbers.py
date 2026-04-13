import numpy as np

class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        for i in matrix:
            unique = list(set(i))
            if len(unique) != len(i):
                return False

        matrix = np.transpose(matrix)

        for i in matrix:
            unique = list(set(i))
            if len(unique) != len(i):
                return False
            

        return True