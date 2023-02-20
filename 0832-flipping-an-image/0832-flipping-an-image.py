class Solution:
    
    def flip(row):
        for i in range(len(row)//2):
            temp = row[i]
            row[i] = row[len(row)-1-i]
            row[len(row)-1-i] = temp 
        return row 
    
    def invert(row):
        for i in range(len(row)):
            if row[i] == 0:
                row[i] = 1 
            else:
                row[i] = 0
        return row
    
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            Solution.flip(row)
            Solution.invert(row)
        
        return image