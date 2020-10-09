class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = float("-inf")
        total = 0
        i = 0
        while i < len(nums):
            total += nums[i]

            maximum = max(maximum, total)

            if total < 0:
                total = 0

            i += 1

        return maximum


