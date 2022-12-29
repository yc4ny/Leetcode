class Solution:
    def getLucky(self, s: str, k: int) -> int:
        alpha = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
                "s","t","u","v","w","x","y","z"]
        string = ''
        for i in range(len(s)):
            string = string + str(alpha.index(s[i]) +1)
        
        for i in range(k):
            liste = []
            for j in range(len(string)):
                liste.append(int(string[j]))
            sumlist = 0 
            for k in range(len(liste)):
                sumlist = sumlist + liste[k]
            string = str(sumlist)
        
        return int(string)