class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0 
        for banks in accounts:
            if sum(banks) > answer:
                answer = sum(banks)
        
        return answer