class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        n = len(nums)
        current_sum = nums[0]
        max_sum = 0

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                current_sum += nums[i]
            else:
                max_sum = max(current_sum, max_sum)
                current_sum = nums[i]

        max_sum = max(current_sum, max_sum)
        
        return max_sum
            