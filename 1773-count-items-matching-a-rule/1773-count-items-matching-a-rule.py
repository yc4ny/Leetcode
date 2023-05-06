class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        if ruleKey == "type":
            for obj in items:
                if obj[0] == ruleValue:
                    count += 1    
        elif ruleKey == "color":
            for obj in items:
                if obj[1] == ruleValue:
                    count += 1       
        
        else: # ruleKey == "name"
            for obj in items:
                if obj[2] == ruleValue:
                    count += 1   
        return count