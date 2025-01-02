class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        merge_word = ''
        for i, j in zip(word1, word2):
            merge_word += i
            merge_word += j

        
        merge_word += word1[len(word2):]
        merge_word += word2[len(word1):]
        
        return merge_word

