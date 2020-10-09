class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # find the upper bound
        # invariant: nums[lo] <= target
        lo, hi = 0, len(nums)
        while hi - lo > 1:
            avg = (lo + hi) // 2

            if nums[avg] <= target:
                lo = avg
            else:
                hi = avg

        # target isn't found
        if len(nums) == 0 or nums[lo] != target:
            return [-1, -1]

        a = lo

        # find lower bound
        # invariant: nums[lo] == target and nums[lo - 1] != target
        lo, hi = 0, len(nums)
        while hi - lo > 1:
            avg = (lo + hi) // 2

            if nums[avg] <= target and nums[avg - 1] != target:
                lo = avg
            else:
                hi = avg

        return [lo, a]
