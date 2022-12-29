class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Dictionary to map string to integer 
        str_num = {"0": 0, "1": 1, "2": 2, "3": 3, "4":4, "5":5, "6" : 6, "7" : 7, "8" : 8, "9" : 9}
        sum_n1 = 0 
        sum_n2 = 0 

        # Calculate individual values of num1, num2 to integer
        for i in range (len(num1)):
            sum_n1 += str_num[num1[i]] * pow(10, len(num1) -1 - i)
        for i in range (len(num2)):
            sum_n2 += str_num[num2[i]] * pow(10, len(num2) -1 - i)

        sum_int = sum_n1 * sum_n2
        return str(sum_int)