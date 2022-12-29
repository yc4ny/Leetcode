class Solution:
    def romanToInt(self, s: str) -> int:
        output = 0; 
        for i in range(len(s)):
            if s[i] == "I": 
                output += 1
            elif s[i] == "V":
                output += 5 
            elif s[i] == "X":
                output += 10  
            elif s[i] == "L":
                output += 50  
            elif s[i] == "C":
                output += 100  
            elif s[i] == "D":
                output += 500  
            elif s[i] == "M":
                output += 1000  
        for i in range (len(s)-1):
            if s[i] == "C" and s[i+1] == "D" or s[i] == "C" and s[i+1] == "M":
                output -= 200 
            if s[i] == "X" and s[i+1] == "L" or s[i] == "X" and s[i+1] == "C":
                output -= 20 
            if s[i] == "I" and s[i+1] == "V" or s[i] == "I" and s[i+1] == "X":
                output -= 2 

        return output