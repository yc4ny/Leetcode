import numpy as np
class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: 
            return n 
        else:
            temp = np.zeros((n+1,1))
            temp[0] = 0
            temp[1] = 1 
            for i in range (2,n+1):
                temp[i] = temp[i-1] + temp[i-2]


        return int(temp[n][0])