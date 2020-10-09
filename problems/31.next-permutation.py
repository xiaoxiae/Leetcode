class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = len(nums) - 1
        while j > 0 and nums[j - 1] >= nums[j]:
            j -= 1

        # go till the first half
        for i in range(((len(nums) - j) // 2)):
            nums[j + i], nums[len(nums) - i - 1] = nums[len(nums) - i - 1], nums[j + i]

        if j == 0:
            return

        for i in range(j, len(nums)):
            if nums[j - 1] < nums[i]:
                nums[j - 1], nums[i] = nums[i], nums[j - 1]
                return
