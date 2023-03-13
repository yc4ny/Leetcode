class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        temp = ""
        for letter in s:
            if letter.isalnum():
                temp += letter
        if temp == temp[::-1]:
            return True 
        else:
            return False