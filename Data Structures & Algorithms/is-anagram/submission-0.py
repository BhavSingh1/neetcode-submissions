class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        s_dict, t_dict = {}, {}

        for elm in range(len(s)):
            s_dict [s[elm]] = 1 + s_dict.get(s[elm], 0)
            t_dict [t[elm]] = 1 + t_dict.get(t[elm], 0)
        return s_dict == t_dict
