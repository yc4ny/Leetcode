class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b=="0":
            return "0"

        a_decimal = 0
        b_decimal = 0 

        for i in range(len(a)):
            a_decimal += int(a[len(a)-1-i]) * pow(2,i) 

        for i in range(len(b)):
            b_decimal += int(b[len(b)-1-i]) * pow(2,i) 

        sum_decimal = a_decimal + b_decimal 
        # print(a_decimal)
        # print(b_decimal)
        print(sum_decimal)
        binary = []

        while (sum_decimal != 1): 
            if sum_decimal % 2 == 1:
                binary.append("1")
            if sum_decimal % 2 == 0:
                binary.append("0")
            sum_decimal = (sum_decimal//2)
            print(sum_decimal)

        answer = "1"
        for i in range(len(binary)):
            answer += binary[len(binary)-1-i]

        return answer