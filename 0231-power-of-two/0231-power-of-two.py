class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        answer = False
        for i in range(31):
            if math.pow(2,i) == n:
                answer = True 
        
        return answer