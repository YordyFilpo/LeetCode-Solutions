class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        index = []
        words = sentence.split()

        for word in range(len(words)):
            if (words[word].startswith(searchWord)):
                index.append(word+1)
        

        if (index):
            return min(index)

        return -1
            