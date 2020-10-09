class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            if target - n in d:
                return d[target - n], i
            d[n] = i
        return -1, -1

    def twoSumSorting(self, nums: List[int], target: int):
        nums = sorted([(e, i) for i, e in enumerate(nums)])

        i, j = 0, len(nums) - 1

        while nums[i][0] + nums[j][0] != target:
            if nums[i][0] + nums[j][0] < target:
                i += 1
            else:
                j -= 1

        return [nums[i][1], nums[j][1]]
