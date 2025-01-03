class Solution:
    import re
    def romanToInt(self, s: str) -> int:
        # Assuming that the inputs are well-formed; thus, not validating input with this solution
        
        romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        integer = 0
        
        for i in range((len(s) - 1)):
            if (romans[s[i]] < romans[s[i+1]]):
                integer -= romans[s[i]]
            else:
                integer += romans[s[i]]

        integer += romans[s[-1]]

        return integer

        # Time Complexity: O(N)

        '''
        Trying a different solution using regex:

        for roman in s:
            ins1 = re.search("IV", s)
            ins2 = re.search("IX", s)
            ins3 = re.search("XL", s)
            ins4 = re.search("XC", s)
            ins5 = re.search("CD", s)
            ins6 = re.search("CM", s)
            if (ins1):
                integer += 4
            elif (ins2):
                integer += 9
            elif (ins3):
                integer += 40
            elif (ins4):
                integer += 90
            elif (ins5):
                integer += 400
            elif (ins6):
                intger += 900 
        '''

        

