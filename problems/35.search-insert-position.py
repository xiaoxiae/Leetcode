class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0 or nums[0] > target:
            return 0

        lo, hi = 0, len(nums)

        # invariant: nums[lo] <=
        while hi - lo > 1:
            avg = (lo + hi) // 2

            if nums[avg] <= target:
                lo = avg
            else:
                hi = avg

        return lo if nums[lo] == target else lo + 1
