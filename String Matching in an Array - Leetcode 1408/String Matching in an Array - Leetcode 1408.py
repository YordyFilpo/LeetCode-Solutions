class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        
        patterns = []

        for i, substring in enumerate(words):
            for j, string in enumerate(words):
                if i != j and substring in string:
                    patterns.append(substring)
                    break
        
        return patterns

        ''' 
        The brute-force solution would be to check if word (one by one) until
        finding the substring IN any of the strings and breaking the iteration
        right away to avoid repeated values in 'patterns'.
        '''

        # Need the 'break' at the end to void this: ['leetcode', 'leetcoder', 'od', 'leetcoder', 'od' 
        # 'leetcode', 'am', 'hamlet']. because I got repetition for one of the substrings in 
        # Test Case #6 without the 'break'.
        
   

