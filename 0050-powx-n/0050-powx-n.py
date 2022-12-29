class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 1 or n == 0:
            return 1
        sign = 1
        if n < 0:
            n *= -1 
            sign = -1
        loop = n
        so_far = 1
        answer = x
        while loop >= so_far*2:
            answer = answer * answer 
            so_far = so_far * 2
        left = loop - so_far
        
        if sign > 0 :
            return answer * Solution.myPow(self, x, left)
        else:
            return 1/(answer * Solution.myPow(self, x, left))

        
        