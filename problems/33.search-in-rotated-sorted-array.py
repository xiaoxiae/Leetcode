class Solution:
    def search(self, nums: List[int], target: int) -> int:
        pivot = 0
        lo, hi = 0, len(nums)

        # invariant: nums[0] <= nums[lo]
        while hi - lo > 1:
            avg = (lo + hi) // 2

            if nums[0] <= nums[avg]:
                lo = avg
            else:
                hi = avg

        pivot = lo + 1

        # invariant: nums[(lo + pivot) % len(nums)] >= target
        lo, hi = 0, len(nums)

        while hi - lo > 1:
            avg = (lo + hi) // 2

            if nums[(avg + pivot) % len(nums)] <= target:
                lo = avg
            else:
                hi = avg

        i = (lo + pivot) % len(nums)
        return i if nums[i] == target else -1
