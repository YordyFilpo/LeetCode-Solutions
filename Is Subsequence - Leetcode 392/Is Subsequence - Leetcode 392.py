class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if not s:
            return True
        elif not t:
            return False

        i = 0
        j = 0

        for j in range(len(t)):
            if i < len(s) and t[j] == s[i]:
                j += 1
                i += 1
            else:
                j += 1
    
        if (i == len(s)):
            return True
        else:
            return False


