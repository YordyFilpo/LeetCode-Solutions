from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        
        universal = []

        def count_char(word):
            return Counter(word)

        max_freq = Counter()
        for word in words2:
            word_count = count_char(word)
            for word, freq in word_count.items():
                max_freq[word] = max(max_freq[word], freq)

        for word in words1:
            word_count = count_char(word)
            if all(word_count[char] >= freq for char, freq in max_freq.items()):
                universal.append(word)
        
        return universal