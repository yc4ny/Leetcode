class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        forward = ""
        backward = ""
        for i in range(len(s)):
            if s[i].isalnum():
                forward += s[i]
            if s[len(s)-1-i].isalnum():
                backward += s[len(s)-1-i]
        if forward == backward:
            return True 
        else:
            return False