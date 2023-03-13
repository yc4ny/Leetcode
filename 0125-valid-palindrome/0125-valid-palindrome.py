class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = [x for x in s if x.isalnum()]
        if s == s[::-1]:
            return True 
        
        return False