import numpy as np 
class Solution:

    def down(row,column):
        row = row + 1
        return row,column

    def up(row, column):
        row = row - 1
        column = column + 1 
        return row, column 

    def convert(self, s: str, numRows: int) -> str:
        s_char = []
        for i in range(len(s)):
            s_char.append(s[i])
        liste = np.zeros((numRows, len(s)), dtype = str)
        row = 0 
        column = 0 
        direction_down = True
        if numRows == 1:
            return s
        else:
            for character in s_char:
                liste[row, column] = character
                if direction_down == True and row < numRows - 1:
                    row,column = Solution.down(row, column)
                    continue
                elif direction_down == True and row == numRows - 1: 
                    direction_down = False
                    row, column = Solution.up(row, column)
                    continue
                elif direction_down == False and row > 0: 
                    row, column = Solution.up(row,column)
                    continue
                elif direction_down == False and row == 0:
                    direction_down = True 
                    row, column = Solution.down(row, column)
            final = ""
            for i in range(liste.shape[0]):
                for j in range(liste.shape[1]):
                    final = final + liste[i][j]
            return final 