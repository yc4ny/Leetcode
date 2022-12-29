class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        sum = 0
        for i in range(length):
            sum += digits[length-1-i]*pow(10,i)
        sum +=1 
        
        sum = str(sum)
        new_digits= []
        for j in range(len(sum)):
            new_digits.append(int(sum[j]))

        
        return new_digits