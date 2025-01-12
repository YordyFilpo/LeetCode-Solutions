class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        open_balance = 0
        for i in range(len(s)):
            if locked[i] == '1' and s[i] == ')':
                open_balance -= 1
            else:
                open_balance += 1
            
            if open_balance < 0:
                return False  
        
        close_balance = 0
        for i in range(len(s) - 1, -1, -1):
            if locked[i] == '1' and s[i] == '(':
                close_balance -= 1
            else:
                close_balance += 1
            
            if close_balance < 0:
                return False  
        return True

        
        