class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        current = 1
        for i in range(len(nums)):
            result[i] *= current
            current *= nums[i]

        current = 1
        for i in reversed(range(len(nums))):
            result[i] *= current
            current *= nums[i]

        return result
