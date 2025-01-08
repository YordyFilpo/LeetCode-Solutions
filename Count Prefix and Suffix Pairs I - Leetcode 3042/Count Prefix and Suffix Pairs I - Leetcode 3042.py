class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        
        # Helper function to get the boolean to determin if str1 is both a prefix and suffix of str2
        def isPrefixAndSuffix(str1, str2):
            return str2.startswith(str1) and str2.endswith(str1)

        counter = 0
        
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if (isPrefixAndSuffix(words[i], words[j])):
                    counter += 1
        
        return counter