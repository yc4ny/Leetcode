class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = ""
        for i in range(len(indices)):
            print(indices.index(i))
            answer = answer + s[indices.index(i)]
        
        return answer