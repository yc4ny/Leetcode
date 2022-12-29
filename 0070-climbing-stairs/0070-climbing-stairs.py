class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 0
        maxNumtwo = int(n/2)
        for i in range(maxNumtwo+1):
            numOnes = n - i*2 
            ways = ways + int((math.factorial(numOnes+i) / (math.factorial(numOnes) * math.factorial(i))))

        return ways 