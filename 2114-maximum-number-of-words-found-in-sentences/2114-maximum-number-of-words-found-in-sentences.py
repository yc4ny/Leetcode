class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        answer = 0
        for sentence in sentences:
            if len(sentence.split(" ")) > answer: 
                answer = len(sentence.split(" "))
        
        return answer 