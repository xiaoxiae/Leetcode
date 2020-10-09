class Solution:
    def maxArea(self, height: List[int]) -> int:
        """The solution essentially boils down to finding next largest from both left
        and right - checking the best right \\foreach left, since smaller will always be
        worse."""
        i, j = 0, len(height) - 1
        i_curr, j_curr = -1, -1
        max_area = 0

        while True:
            # find next bigger line
            while i_curr >= height[i] and i < j:
                i += 1
            i_curr = height[i]

            if i == j:
                break

            # find all smaller increasing lines from the right
            while i_curr > j_curr:
                while j_curr >= height[j] and i < j:
                    j -= 1

                j_curr = height[j]

                if min(i_curr, j_curr) * (j - i) > max_area:
                    max_area = min(i_curr, j_curr) * (j - i)

            j_curr = -1

        return max_area
