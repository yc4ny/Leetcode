class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        answer = []
        for i in range(left, right+1):
            i_string = str(i)
            a = True
            for j in range(len(i_string)):
                if int(i_string[j]) == 0:
                    a = False
                elif i%int(i_string[j]) != 0:
                    a = False
            if a:
                answer.append(i)
            
        return answer