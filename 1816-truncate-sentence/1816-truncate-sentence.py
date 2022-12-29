class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        liste = s.split()
        string = ""
        for i in range(k):
            if i != k-1:
                string = string + liste[i] + " "
            else:
                string = string + liste[i]
        
        return string