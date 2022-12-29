class Solution:
    def factorial(i):
        output = 1
        for i in range(2, i +1):
            output *= i
        return output

    def uniquePaths(self, m: int, n: int) -> int:
        ans = factorial(m+n -2) / (factorial(m-1) * factorial(n-1)) 
        return int(ans)