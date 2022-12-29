class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        combined = []
        for i in range(len(words1)):
            combined.append(words1[i])
        for i in range(len(words2)):
            combined.append(words2[i])
            
        combined = list(set(combined))
        total = 0 
        for i in range(len(combined)): 
            if combined[i] in words1 and combined[i] in words2:
                count1 = 0 
                count2 = 0 
                for j in range(len(words1)):
                    if words1[j] == combined[i]:
                        count1 += 1 
                for k in range(len(words2)):
                    if words2[k] == combined[i]:
                        count2 += 1
                if count1 == 1 and count2 == 1:
                    total += 1 
        
        return total