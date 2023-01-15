class Solution:
    def defangIPaddr(self, address: str) -> str:
        answer = ""
        for item in address:
            if item != ".":
                answer = answer + item
            else:
                answer = answer + '[.]'
        return answer