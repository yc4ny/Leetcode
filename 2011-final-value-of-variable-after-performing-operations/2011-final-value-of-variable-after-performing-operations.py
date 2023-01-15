class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0 
        for value in operations:
            if value[0] == "-" or value[1] == "-":
                answer -= 1
            else:
                answer += 1
        
        return answer
                