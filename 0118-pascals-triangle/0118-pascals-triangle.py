class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        liste = []
        for i in range(1,numRows +1):
            liste.append([1] * i)
        
        for i in range(len(liste)):
            if len(liste[i]) > 2:
                for j in range(1,len(liste[i])-1):
                    liste[i][j] = liste[i-1][j-1] + liste[i-1][j]
        return liste
                    
        
            
                