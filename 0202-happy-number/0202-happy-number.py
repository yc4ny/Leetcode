class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 2 or n ==3 or n == 4:
            return False
        
        n_s = str(n)
        n = 0
        for i in range(len(n_s)):
            n += int(n_s[i]) * int(n_s[i])
 
        return Solution.isHappy(self,n)
    
        