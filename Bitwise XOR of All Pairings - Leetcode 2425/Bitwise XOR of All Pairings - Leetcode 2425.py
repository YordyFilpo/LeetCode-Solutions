class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        nums3 = []
        xor1 = 0
        xor2 = 0        
        bitwise_value = 0

        for num in nums1:
            xor1 ^= num
        
        for num in nums2:
            xor2 ^= num
        
        if len(nums1) % 2 != 0:
            bitwise_value ^= xor2
        if len(nums2) % 2 != 0:
            bitwise_value ^= xor1
        return bitwise_value
         
            
 
        