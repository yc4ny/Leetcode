class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum_digit = 0 
        product_digit = 1
        for digit in str(n):
            sum_digit += int(digit)
            product_digit *= int(digit) 
        
        return product_digit - sum_digit