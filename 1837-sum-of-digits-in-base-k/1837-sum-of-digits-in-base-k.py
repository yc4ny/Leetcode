class Solution:
    def sumBase(self, n: int, k: int) -> int:
        stop = False 
        max_base = 0
        while stop is False:
            if n - pow(k, max_base) >= 0:
                max_base += 1 
            else:
                stop = True 
        max_base -= 1
        
        digits = []
        
        while max_base >= 0:
            digit = n //pow(k, max_base)
            digits.append(digit)
            n = n - digit * pow(k,max_base)
            max_base -= 1
        
        return sum(digits)