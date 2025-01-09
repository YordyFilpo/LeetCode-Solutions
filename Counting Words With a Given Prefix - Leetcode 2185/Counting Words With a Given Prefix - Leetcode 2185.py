class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        
        prefix_count = 0
        for word in words:
            if (word.startswith(pref)):
                prefix_count += 1
        
        return prefix_count