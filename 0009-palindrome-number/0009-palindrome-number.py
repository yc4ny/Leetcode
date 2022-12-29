class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Converting Int to String solution 
        s = str(x)
        j = s
        for i in range(int(len(s)/2)):
            if j[i] == s[len(s)-1-i]:
                continue
            else:
                return False

        return True 