class Solution:
    def maximum69Number (self, num: int) -> int:
        num = str(num)
        answer = ""
        stop = False
        for i in range(len(num)):
            if num[i] =="6" and stop is False:
                answer += "9" 
                stop = True
            else:
                answer += str(num)[i]
        return int(answer)