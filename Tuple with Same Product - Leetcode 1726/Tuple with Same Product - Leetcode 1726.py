class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        total_pairs = 0
        product_counter = defaultdict(int)
        pair_counter = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
                pair_counter[product] += product_counter[product]
                product_counter[product] += 1
                
        
        for counter in pair_counter.values():
            total_pairs += 8 * counter
        
        return total_pairs