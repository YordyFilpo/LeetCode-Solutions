from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        freq = Counter(s)
        length_after = 0
        
        for c, count_c in freq.items():
            if count_c < 3:
                # Can't remove anything if we have fewer than 3
                length_after += count_c
            else:
                if count_c % 2 == 1:
                    length_after += 1  # reduce to 1 if odd
                else:
                    length_after += 2  # reduce to 2 if even
        return length_after
