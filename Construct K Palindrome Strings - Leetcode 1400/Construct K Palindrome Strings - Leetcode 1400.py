class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # Step 1: If k > length of string, it's impossible
        if k > len(s):
            return False
        
        # Step 2: Count character frequencies
        char_count = Counter(s)
        
        # Step 3: Count odd frequencies
        odd_count = sum(1 for count in char_count.values() if count % 2 != 0)
        
        # Step 4: Check if k >= odd_count
        return k >= odd_count