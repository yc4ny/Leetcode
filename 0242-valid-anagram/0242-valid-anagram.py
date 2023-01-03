class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        s_list = []
        t_list = []
        for i in range(len(s)):
            s_list.append(s[i])
            t_list.append(t[i])
        if sorted(s_list) == sorted(t_list):
            return True 
        else:
            return False
        