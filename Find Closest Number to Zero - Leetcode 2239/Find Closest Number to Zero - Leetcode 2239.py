class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        
        close_num = nums[0]
        
        for num in nums:
            if abs(num) < abs(close_num):
                close_num = num
            elif abs(num) == abs(close_num) and num > close_num:
                close_num = num
        
        return close_num

   