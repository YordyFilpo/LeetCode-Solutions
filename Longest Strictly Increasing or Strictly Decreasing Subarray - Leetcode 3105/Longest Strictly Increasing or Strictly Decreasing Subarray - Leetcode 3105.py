class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing_len = 1
        decreasing_len = 1
        max_len = 1
        n = len(nums)

        if n == 1:
            return 1

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                increasing_len += 1
                decreasing_len = 1

            elif nums[i] < nums[i-1]:
                decreasing_len += 1
                increasing_len = 1
            
            else:
                decreasing_len = 1
                increasing_len = 1

            max_len = max(max_len, increasing_len, decreasing_len)

        return max_len